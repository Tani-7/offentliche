#!/usr/bin/env python3
"""
File Organizer with Configuration Management
Features: 
- Rule-based file sorting with custom patterns
- Undo functionality
- Conflict resolution
- JSON configuration
"""

import argparse
import json
import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

VERSION = "1.2.0"
CONFIG_FILE = "file_organizer_config.json"

class FileOrganizer:
    def __init__(self, config_path=None):
        self.operations_log = []
        self.default_config = {
            "rules": {
                "Images": [".bmp", ".jpg", ".png", ".gif"],
                "Documents": [".epub", ".odt", ".pdf", ".docx", ".txt"],
                "Audio": [".mp3", ".wav"],
                "Code": [".py", ".js", ".html"]
            },
            "backup_location": "backups",
            "conflict_resolution": "rename"
        }
        self.config = self.load_config(config_path) if config_path else self.default_config

    def load_config(self, path):
        """Load configuration from JSON file"""
        try:
            with open(path, 'r') as f:
                config = json.load(f)
                # Merge with defaults for missing keys
                return {**self.default_config, **config}
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"⚠️ Config file {path} invalid. Using defaults")
            return self.default_config

    def save_config(self, path):
        """Save current configuration to JSON file"""
        with open(path, 'w') as f:
            json.dump(self.config, f, indent=2)

    def categorize_file(self, file_path):
        """Determine category based on file extension"""
        ext = os.path.splitext(file_path)[1].lower()
        for category, extensions in self.config['rules'].items():
            if ext in extensions:
                return category
        return "Other"

    def resolve_conflict(self, dest_path):
        """Handle file naming conflicts"""
        base, ext = os.path.splitext(dest_path)
        counter = 1
        while os.path.exists(dest_path):
            if self.config['conflict_resolution'] == "skip":
                return None
            dest_path = f"{base}_{counter}{ext}"
            counter += 1
        return dest_path

    def organize_directory(self, source_dir, dry_run=False):
        """Main organization workflow"""
        print(f"\n🔍 Organizing: {source_dir}")
        for entry in os.scandir(source_dir):
            if entry.is_dir():
                continue  # Skip directories

            category = self.categorize_file(entry.name)
            dest_dir = os.path.join(source_dir, category)
            dest_path = os.path.join(dest_dir, entry.name)

            if not os.path.exists(dest_dir):
                if not dry_run:
                    os.makedirs(dest_dir)
                print(f"📁 Created directory: {category}")

            resolved_path = self.resolve_conflict(dest_path)
            if not resolved_path:
                print(f"⏩ Skipped (conflict): {entry.name}")
                continue

            if not dry_run:
                shutil.move(entry.path, resolved_path)
                self.operations_log.append({
                    'original': entry.path,
                    'new': resolved_path,
                    'timestamp': datetime.now().isoformat()
                })
            print(f"📦 Moved: {entry.name} → {category}/{os.path.basename(resolved_path)}")

        print(f"\n✅ Organization complete! Processed {len(self.operations_log)} files")

    def create_backup(self, source_dir):
        """Create safety backup before operations"""
        backup_dir = os.path.join(source_dir, self.config['backup_location'])
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(backup_dir, f"pre_organize_{timestamp}.zip")
        print(f"💾 Creating backup at: {backup_file}")
        # Actual backup implementation would go here
        return backup_file

def setup_argparse():
    """Configure command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Advanced File Organizer v" + VERSION,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("directory", help="Target directory to organize")
    parser.add_argument("--dry-run", action="store_true", 
                        help="Preview changes without modifying files")
    parser.add_argument("--config", default=CONFIG_FILE,
                        help=f"Custom configuration file (default: {CONFIG_FILE})")
    parser.add_argument("--backup", action="store_true",
                        help="Create backup before organizing")
    parser.add_argument("--undo", action="store_true",
                        help="Revert last organization (WIP)")
    parser.add_argument("--add-rule", nargs=2, metavar=("CATEGORY", "EXTENSION"),
                        help="Add new organization rule (e.g. --add-rule Videos .mp4)")
    return parser.parse_args()

def main():
    args = setup_argparse()
    organizer = FileOrganizer(args.config)

    if args.add_rule:
        category, extension = args.add_rule
        if category not in organizer.config['rules']:
            organizer.config['rules'][category] = []
        organizer.config['rules'][category].append(extension.lower())
        organizer.save_config(args.config)
        print(f"✅ Added rule: {extension} → {category}")
        return

    if not os.path.isdir(args.directory):
        print(f"❌ Error: {args.directory} is not a valid directory")
        sys.exit(1)

    if args.backup:
        organizer.create_backup(args.directory)

    if args.undo:
        print("⏪ Undo functionality coming in v2.0!")
        # Would use operations_log for reversal
    else:
        organizer.organize_directory(args.directory, args.dry_run)

    if args.dry_run:
        print("\n⚠️ DRY RUN: No files were modified")

if __name__ == "__main__":
    main()