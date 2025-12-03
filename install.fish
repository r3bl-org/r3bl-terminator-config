#!/usr/bin/env fish
# Install r3bl-terminator-config
# Copies the Terminator config and plugin to ~/.config/terminator/

set script_dir (dirname (status filename))
set terminator_dir ~/.config/terminator
set plugins_dir $terminator_dir/plugins

echo "Installing r3bl-terminator-config..."

# Create directories if they don't exist
mkdir -p $terminator_dir
mkdir -p $plugins_dir

# Copy config file
cp $script_dir/config $terminator_dir/config
echo "Copied config to $terminator_dir/config"

# Copy plugin
cp $script_dir/plugins/claude_code_shortcut.py $plugins_dir/
echo "Copied plugin to $plugins_dir/claude_code_shortcut.py"

echo "Done! Restart Terminator to apply changes."
