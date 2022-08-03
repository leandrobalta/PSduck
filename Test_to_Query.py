from re import T
from psutil import sensors_battery, swap_memory, cpu_count, cpu_stats, cpu_percent, cpu_freq, disk_io_counters, disk_partitions, disk_usage, sensors_temperatures


# print(swap_memory())
# print(cpu_count())
# print(cpu_stats())
print(cpu_freq(cpu_percent(percpu=True)))

# print(cpu_percent(pe))


print()
print()
print()

print(cpu_percent())


print()
print()
print()

print(disk_usage('/'))

print()
print()
print()

for i in enumerate(disk_usage('/')):
    print(i)

print()
print()
print()


for i in sensors_temperatures():
    print(i)

print()

test = (sensors_temperatures()['coretemp'][0])

print(f" {test.current}C")

print()
print()
print()

battery_percent = sensors_battery()
print(battery_percent.percent)
