import toml

# Load the existing TOML file
file_path = 'Cargo.toml'
data = toml.load(file_path)

# Keys to delete
keys_to_delete = [
    'features.rustc-dep-of-std',
    'dependencies.compiler_builtins',
    'dependencies.core',
    'dependencies.rustc-std-workspace-alloc',
    'lib.bench'
]

# Delete the specified keys
for key in keys_to_delete:
    parts = key.split('.')
    current_level = data
    for part in parts[:-1]:
        current_level = current_level.get(part, {})
    if parts[-1] in current_level:
        del current_level[parts[-1]]

# Save the modified TOML back to the file
with open(file_path, 'w') as f:
    toml.dump(data, f)

print("Keys deleted successfully.")
