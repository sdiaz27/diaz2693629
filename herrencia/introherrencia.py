class vehicle:
    pass
class landVehicle(vehicle):
    pass
class trackVehicle(landVehicle):
    pass
for cls1 in [vehicle, landVehicle, trackVehicle]:
    for cls2 in [vehicle, landVehicle, trackVehicle]:
        print(issubclass(cls1, cls2), end="\t")
    print()