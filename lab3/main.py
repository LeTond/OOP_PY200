import Builders
import LinkedL


driver_name = input("Please enter driver name -> ")
driver_builder = Builders.SDFabric.get_sd_driver(driver_name)

new_list = LinkedL.LinkedList()
new_list.set_structure_driver(driver_builder.build())
new_list.append('zero data')
new_list.append('first data')
new_list.insert('fourth data', 0)
new_list.insert('fifth data', 6)
new_list.insert('sixth data', 1)
new_list.insert('seventh data', 0)
new_list.append('zero')
new_list.append('first')
new_list.delete(1)
new_list.delete(3)

# new_list.clear()
