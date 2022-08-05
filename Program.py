from psutil import (
    cpu_percent,
    cpu_freq,
    disk_partitions,
    disk_usage,
    virtual_memory,
    swap_memory,
    sensors_temperatures,
    sensors_battery,
    disk_usage,
    users
)
from dashing import HSplit, VSplit, VGauge, HGauge, Text
from time import sleep

user_interface = HSplit(  # user_interface have items
    HSplit(  # RAM -->   user_interface.items[0]
        # user_interface.items[0].items[0] -> this is to access this scope of the "user_interface"

        VGauge(title="RAM"),
        VGauge(title='SWAP'),
        title="MEMORY",
        border_color=2
    ),
    VSplit(  # CPU --> user_interface.items[1]

        HGauge(title='CPU (MAIN)'),
        HGauge(title='CPU_1'),
        HGauge(title='CPU_2'),
        HGauge(title='CPU_3'),
        HGauge(title='CPU_4'),
        HGauge(title='CPU TEMP'),
        title="CPU MONITOR",
        border_color=5
    ),
    VSplit(  # DISK AND OTHERS --> user_interface.items[2]
        Text(  # DISK --> user_interface.items[2].items[0]
            ' ',
            title="DISK INFO",
            border_color=1,
        ),
        VSplit(  # OTHERS --> user_interface.items[2].items[1]
            Text(  # user_interface.items[2].items[1].items[0]
                ' ',


            ),
            Text(  # user_interface.items[2].items[1].items[1]
                ' ',

            ),
            title="OTHERS",
            border_color=3,

        ),


    )
)


def ConvertToGiga(value):
    return value / 1024 / 1024 / 1024


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

    # the other cpu cores
    cpu_cores_ui = cpu_ui.items[1:5]
    all_cores_percent = cpu_percent(percpu=True)

    for i, (core, value) in enumerate(zip(cpu_cores_ui, all_cores_percent)):
        core.value = value
        core.title = f" CPU_{i + 1} {value}%"

    # cpu temperature
    cpu_temp_ui = cpu_ui.items[5]
    temp = sensors_temperatures()['coretemp'][0]
    cpu_temp_ui.value = temp.current
    cpu_temp_ui.title = f" CPU TEMP {cpu_temp_ui.value}C"

    # --------------------------------------------------

    # DISK
    disk_ui = user_interface.items[2].items[0]
    disk_used = disk_usage('/')
    used = ConvertToGiga(disk_used.used)
    disk_ui.value = used
    disk_ui.text = f"DISK USED {disk_ui.value:.2f}GB"

    # --------------------------------------------------

    # OTHERS

    # battery
    battery_ui = user_interface.items[2].items[1].items[0]
    battery = sensors_battery()
    battery_ui.value = battery.percent
    battery_ui.text = f" BATTERY {battery_ui.value:.2f}%"

    # user
    user_ui = user_interface.items[2].items[1].items[1]
    user_ui = users()[0]
    user_ui.value = user_ui
    user_ui.text = f'{user_ui.name}'

    try:
        user_interface.display()
        sleep(.5)
    except KeyboardInterrupt:
        break
