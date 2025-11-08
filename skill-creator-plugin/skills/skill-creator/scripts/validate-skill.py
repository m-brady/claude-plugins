#!/usr/bin/env python3
"""
Validate a Claude Code SKILL.md file.

Usage:
    python validate-skill.py path/to/SKILL.md
"""

import re
import sys
from pathlib import Path
from typing import Tuple, List

# Validation rules
NAME_PATTERN = re.compile(r'^[a-z0-9-]+$')
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024

def validate_yaml_frontmatter(content: str) -> Tuple[bool, List[str], dict]:
    """
    Validate YAML frontmatter in SKILL.md.

    Returns:
        Tuple of (is_valid, errors, frontmatter_data)
    """
    errors = []
    frontmatter_data = {}

    lines = content.split('\n')

    # Check first line is ---
    if not lines or lines[0].strip() != '---':
        errors.append("YAML frontmatter must start with '---' on line 1")
        return False, errors, frontmatter_data

    # Find closing ---
    closing_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == '---':
            closing_idx = i
            break

    if closing_idx is None:
        errors.append("YAML frontmatter must end with '---'")
        return False, errors, frontmatter_data

    # Extract frontmatter
    frontmatter_lines = lines[1:closing_idx]

    # Parse YAML (simple parsing for validation)
    for line in frontmatter_lines:
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            # Remove quotes if present
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]

            frontmatter_data[key] = value

    # Check required fields
    if 'name' not in frontmatter_data:
        errors.append("Missing required field: 'name'")

    if 'description' not in frontmatter_data:
        errors.append("Missing required field: 'description'")

    return len(errors) == 0, errors, frontmatter_data


def validate_name(name: str) -> Tuple[bool, List[str]]:
    """Validate skill name."""
    errors = []

    if not name:
        errors.append("Name cannot be empty")
        return False, errors

    if len(name) > MAX_NAME_LENGTH:
        errors.append(f"Name exceeds maximum length of {MAX_NAME_LENGTH} characters (got {len(name)})")

    if not NAME_PATTERN.match(name):
        errors.append(f"Name must contain only lowercase letters, numbers, and hyphens (got: '{name}')")

        # Provide specific feedback
        if any(c.isupper() for c in name):
            errors.append("  - Contains uppercase letters (use lowercase only)")
        if '_' in name:
            errors.append("  - Contains underscores (use hyphens instead)")
        if ' ' in name:
            errors.append("  - Contains spaces (use hyphens instead)")
        if any(c in name for c in '!@#$%^&*()+=[]{}|\\;:\'",.<>?/'):
            errors.append("  - Contains special characters (only hyphens allowed)")

    return len(errors) == 0, errors


def validate_description(description: str) -> Tuple[bool, List[str]]:
    """Validate skill description."""
    errors = []
    warnings = []

    if not description:
        errors.append("Description cannot be empty")
        return False, errors

    if len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(f"Description exceeds maximum length of {MAX_DESCRIPTION_LENGTH} characters (got {len(description)})")

    # Check for best practices (warnings, not errors)
    description_lower = description.lower()

    if 'use when' not in description_lower:
        warnings.append("Description should include 'Use when' to indicate when to activate this skill")

    if len(description) < 50:
        warnings.append("Description is quite short - consider adding more detail about what it does and when to use it")

    # Check for vague terms
    vague_terms = ['helps', 'assists', 'general', 'various', 'stuff', 'things']
    found_vague = [term for term in vague_terms if term in description_lower]
    if found_vague:
        warnings.append(f"Description contains vague terms: {', '.join(found_vague)}. Be more specific.")

    if warnings:
        print("\n⚠️  Warnings (not errors, but consider addressing):")
        for warning in warnings:
            print(f"  - {warning}")

    return len(errors) == 0, errors


def validate_file_structure(skill_path: Path) -> Tuple[bool, List[str]]:
    """Validate the skill file structure."""
    errors = []
    warnings = []

    skill_md = skill_path
    skill_dir = skill_path.parent

    if not skill_md.exists():
        errors.append(f"SKILL.md not found at {skill_md}")
        return False, errors

    # Check for supporting files referenced in SKILL.md
    content = skill_md.read_text()

    # Find markdown links and code references
    link_pattern = re.compile(r'\[([^\]]+)\]\(([^\)]+)\)')
    matches = link_pattern.findall(content)

    for link_text, link_path in matches:
        # Skip external links
        if link_path.startswith('http://') or link_path.startswith('https://'):
            continue

        # Check if referenced file exists
        referenced_file = skill_dir / link_path
        if not referenced_file.exists():
            warnings.append(f"Referenced file not found: {link_path}")

    if warnings:
        print("\n⚠️  File Structure Warnings:")
        for warning in warnings:
            print(f"  - {warning}")

    return len(errors) == 0, errors


def validate_skill_file(skill_path: Path) -> bool:
    """
    Validate a complete SKILL.md file.

    Returns:
        True if valid, False otherwise
    """
    print(f"Validating: {skill_path}\n")

    if not skill_path.exists():
        print(f"❌ Error: File not found: {skill_path}")
        return False

    content = skill_path.read_text()
    all_valid = True

    # Validate YAML frontmatter
    print("Checking YAML frontmatter...")
    valid_yaml, yaml_errors, frontmatter = validate_yaml_frontmatter(content)

    if not valid_yaml:
        print("❌ YAML frontmatter errors:")
        for error in yaml_errors:
            print(f"  - {error}")
        all_valid = False
    else:
        print("✅ YAML frontmatter is valid")

        # Validate name
        if 'name' in frontmatter:
            print("\nChecking name...")
            valid_name, name_errors = validate_name(frontmatter['name'])
            if not valid_name:
                print("❌ Name validation errors:")
                for error in name_errors:
                    print(f"  - {error}")
                all_valid = False
            else:
                print(f"✅ Name is valid: '{frontmatter['name']}'")

        # Validate description
        if 'description' in frontmatter:
            print("\nChecking description...")
            valid_desc, desc_errors = validate_description(frontmatter['description'])
            if not valid_desc:
                print("❌ Description validation errors:")
                for error in desc_errors:
                    print(f"  - {error}")
                all_valid = False
            else:
                print(f"✅ Description is valid ({len(frontmatter['description'])} characters)")

        # Validate allowed-tools if present
        if 'allowed-tools' in frontmatter:
            print("\nChecking allowed-tools...")
            print(f"✅ Tool restrictions found: {frontmatter['allowed-tools']}")

    # Validate file structure
    print("\nChecking file structure...")
    valid_structure, structure_errors = validate_file_structure(skill_path)
    if not valid_structure:
        print("❌ File structure errors:")
        for error in structure_errors:
            print(f"  - {error}")
        all_valid = False
    else:
        print("✅ File structure is valid")

    # Summary
    print("\n" + "="*60)
    if all_valid:
        print("✅ Skill validation PASSED")
        print("\nYour skill is ready to use!")
        print("Remember to restart Claude Code to load the new skill.")
    else:
        print("❌ Skill validation FAILED")
        print("\nPlease fix the errors above and try again.")
    print("="*60)

    return all_valid


def main():
    if len(sys.argv) != 2:
        print("Usage: python validate-skill.py path/to/SKILL.md")
        sys.exit(1)

    skill_path = Path(sys.argv[1])
    valid = validate_skill_file(skill_path)

    sys.exit(0 if valid else 1)


if __name__ == '__main__':
    main()
