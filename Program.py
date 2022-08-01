from psutil import (
    cpu_percent,
    cpu_freq,
    virtual_memory,
    swap_memory
)
from dashing import HSplit, VSplit, VGauge, HGauge
from time import sleep

user_interface = HSplit(  # user_interface have items
    HSplit(  # RAM -->   user_interface.items[0]
        # user_interface.items[0].items[0] -> this is to access this scope of the "user_interface"
        VGauge(title="RAM"),
        VGauge(title='SWAP'),
        title="MEMORY",
        border_color=2
    ),
    HSplit(
        HGauge(title='CPU'),
        title="CPU MONITOR",
        border_color=5
    )
)

while True:
    # MEMORY
    memory_ui = user_interface.items[0]

    # ram
    ram_ui = memory_ui.items[0]
    ram_ui.value = virtual_memory().percent
    ram_ui.title = f" RAM {ram_ui.value}%"

    # swap
    swap_ui = memory_ui.items[1]
    swap_ui.value = swap_memory().percent
    swap_ui.title = f" SWAP {swap_ui.value}%"

    # ----------------------------------------
    # CPU MONITOR
    cpu_ui = user_interface.items[1]

    # principal cpu
    principal_cpu = cpu_ui.items[0]
    principal_cpu.value = cpu_percent()
    principal_cpu.title = f" CPU {principal_cpu.value}%"

    try:
        user_interface.display()
        sleep(.5)
    except KeyboardInterrupt:
        break
