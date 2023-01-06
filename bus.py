class Bus:

    def __init__(self, id, from_destination, to_destination, seats):
        self.id = id
        self.from_destination = from_destination
        self.to_destination = to_destination
        self.seats = seats
        self.booked_seats =[]

buses = [
  {'number': 1, 'route': 'Gaza to Jerusalem', 'seats': ['1A','2A','3A','4A','5A','6A','7A','8A','9A','10A','11A',
                                                        '1B','2B','3B','4B','5B','6B','7B','8B','9B','10B','11B',
                                                        '1C','2C','3C','4C','5C','6C','7C','8C','9C','10C','11C',
                                                        '1D','2D','3D','4D','5D','6D','7D','8D','9D','10D','11D',
                                                        '1E','2E','3E','4E','5E','6E'], 'reserved_seats': []},

  {'number': 2, 'route': 'Gaza to Jaffa', 'seats': ['1A','2A','3A','4A','5A','6A','7A','8A','9A','10A','11A',
                                                        '1B','2B','3B','4B','5B','6B','7B','8B','9B','10B','11B',
                                                        '1C','2C','3C','4C','5C','6C','7C','8C','9C','10C','11C',
                                                        '1D','2D','3D','4D','5D','6D','7D','8D','9D','10D','11D',
                                                        '1E','2E','3E','4E','5E','6E'], 'reserved_seats': []},

  {'number': 3, 'route': 'Gaza to Jericho', 'seats': ['1A','2A','3A','4A','5A','6A','7A','8A','9A','10A','11A',
                                                        '1B','2B','3B','4B','5B','6B','7B','8B','9B','10B','11B',
                                                        '1C','2C','3C','4C','5C','6C','7C','8C','9C','10C','11C',
                                                        '1D','2D','3D','4D','5D','6D','7D','8D','9D','10D','11D',
                                                        '1E','2E','3E','4E','5E','6E'], 'reserved_seats': []}
]

def show_buses():
  print('Buses:')
  for i, bus in enumerate(buses):
    print(f'{i+1}. Bus number {bus["number"]} ({bus["route"]})')

def show_seats(bus):
    available_seats = [seat for seat in bus['seats'] if seat not in bus['reserved_seats']]
    print(f'Seats available for bus {bus["number"]} ({bus["route"]}): {available_seats}')

def reserve_seat(bus, seat):
  if seat in bus['seats'] and seat not in bus['reserved_seats']:
    bus['reserved_seats'].append(seat)
    print(f'Seat {seat} successfully reserved for bus {bus["number"]} ({bus["route"]})')
  elif seat in bus['reserved_seats']:
    print(f'Seat {seat} is already reserved for bus {bus["number"]} ({bus["route"]})')
  else:
    print(f'Seat {seat} is not available for bus {bus["number"]} ({bus["route"]})')

def cancel_reservation(bus, seat):
  if seat in bus['reserved_seats']:
    bus['reserved_seats'].remove(seat)
    print(f'Reservation for seat {seat} on bus {bus["number"]} ({bus["route"]}) successfully canceled')
  else:
    print(f'Seat {seat} is not reserved on bus {bus["number"]} ({bus["route"]})')

while True:
    print('Enter 1 to view available buses')
    print('Enter 2 to make a reservation')
    print('Enter 3 to cancel a reservation')
    print('Enter 4 to exit the program')
    choice = input('Enter your choice: ')
    if choice == '1':
        show_buses()
        print('this is all bus')
    elif choice == '2':
        bus_number = int(input('Enter the bus number: '))
        bus = next(bus for bus in buses if bus['number'] == bus_number)
        show_seats(bus)
        seat = input('Enter the seat number: ')
        print()
        reserve_seat(bus, seat)
    elif choice =='3':
        bus_number = int(input('Enter the bus number: '))
        seat = input('Enter the seat number: ')
        bus = next(bus for bus in buses if bus['number'] == bus_number)
        cancel_reservation(bus, seat)
    elif choice == '4':
        break
    else:
        print('Invalid choice')