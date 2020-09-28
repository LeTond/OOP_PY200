import Builders
import LinkedList


driver_name = input("Please enter driver name -> ")
driver_builder = Builders.SDFabric.get_sd_driver(driver_name)

new_list = LinkedList.LinkedList()
new_list.append('zero data')
new_list.append('first data')
new_list.append('second data')
new_list.append('third data')
new_list.insert('fourth data', 3)
new_list.insert('fifth data', 6)
new_list.insert('sixth data', 1)
new_list.insert('seventh data', 0)

new_list.set_structure_driver(driver_builder.build())
new_list.save()
new_list.load()
