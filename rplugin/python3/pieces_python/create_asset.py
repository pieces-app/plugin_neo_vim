from ._pieces_lib import pieces_os_client as pos_client
from .settings import Settings


def get_data():
	buf = Settings.nvim.current.buffer
	mode = Settings.nvim.api.get_mode()['mode']


	if mode in {'v', 'V', '\x16'}:
		start_pos = Settings.nvim.api.get_pos('\'<')
		end_pos = Settings.nvim.api.get_pos('\'>')

		# Convert to line and column format
		start_line, start_col = start_pos[0] - 1, start_pos[1] - 1
		end_line, end_col = end_pos[0] - 1, end_pos[1]

		# Get the lines in the selection
		lines = buf[start_line:end_line + 1]

		# If there's more than one line, handle multi-line selection
		if len(lines) > 1:
			lines[-1] = lines[-1][:end_col]
			lines[0] = lines[0][start_col:]
		else:
			lines[0] = lines[0][start_col:end_col]

		# Join lines and return the selected text
		return '\n'.join(lines)
	else:
		Settings.nvim.err_write("Error: No code selected in visual mode. Please select some code and try again.\n")
		return ""


def create_asset(data,ext=None):
	if not data: return
	seed = get_seeds(data,ext)
	assets_api = pos_client.AssetsApi(Settings.api_client)
	created_asset_id = assets_api.assets_create_new_asset(transferables=False, seed=seed).id
	Settings.nvim.out_write("Snippet created successfully!\n")
	return created_asset_id

def get_seeds(data,ext=None):
	# Getting the metadata
	if ext in pos_client.ClassificationSpecificEnum:
		metadata = pos_client.FragmentMetadata(ext=ext)
	else:
		metadata = None
	

	# Construct a Seed
	seed = pos_client.Seed(
		asset=pos_client.SeededAsset(
			application=Settings.get_application(),
				format=pos_client.SeededFormat(
						fragment=pos_client.SeededFragment(
							string=pos_client.TransferableString(raw=data),
							metadata=metadata
						)
					),
				metadata=None
			),
		type="SEEDED_ASSET"
	)
	return seed