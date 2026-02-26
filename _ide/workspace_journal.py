# 2026-02-25T14:19:34.085930500
import vitis

client = vitis.create_client()
client.set_workspace(path="lab2")

platform = client.get_component(name="lab2")
status = platform.build()

comp = client.create_app_component(name="lab2_part1",platform = "$COMPONENT_LOCATION/../lab2/export/lab2/lab2.xpfm",domain = "freertos_ps7_cortexa9_0")

comp = client.get_component(name="lab2_part1")
status = comp.import_files(from_loc="", files=["C:\Users\jkodei\Documents\lab2_part1.c", "C:\Users\jkodei\Documents\sha256.c", "C:\Users\jkodei\Documents\sha256.h", "C:\Users\jkodei\Documents\uart_driver.c", "C:\Users\jkodei\Documents\uart_driver.h"])

status = comp.import_files(from_loc="$COMPONENT_LOCATION/../../../Downloads", files=["lab1_part3.c"], dest_dir_in_cmp = "lab2_part1")

status = platform.build()

comp = client.get_component(name="lab2_part1")
comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

client.delete_component(name="lab2_part1")

comp = client.create_app_component(name="lab2_part1",platform = "$COMPONENT_LOCATION/../lab2/export/lab2/lab2.xpfm",domain = "freertos_ps7_cortexa9_0")

comp = client.get_component(name="lab2_part1")
status = comp.import_files(from_loc="", files=["C:\Users\jkodei\Documents\lab2_part1.c", "C:\Users\jkodei\Documents\sha256.c", "C:\Users\jkodei\Documents\sha256.h", "C:\Users\jkodei\Documents\uart_driver.c", "C:\Users\jkodei\Documents\uart_driver.h"])

status = platform.build()

comp = client.get_component(name="lab2_part1")
comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

status = platform.build()

comp.build()

vitis.dispose()

