import datetime


class Country:
    def __init__(self, countryID=0, name=""):
        self.__countryID = countryID
        self.__name = name

    @property
    def countryID(self):
        return self.__countryID

    @property
    def name(self):
        return self.__name

    def __str__(self) -> str:
        return 'Country {' + '\n' + \
               '\t' + 'countryID: ' + str(self.__countryID) + '\n' + \
               '\t' + 'name: ' + self.__name + '\n' + \
               '\t' + '}' + '\n'


class Location:
    def __init__(self, postCode="", outerCode="", region="", town=""):
        self.__postCode = postCode
        self.__outerCode = outerCode
        self.__region = region
        self.__outerCode = outerCode
        self.__town = town

    @property
    def postCode(self):
        return self.__postCode

    @property
    def outerCode(self):
        return self.__outerCode

    @property
    def region(self):
        return self.__region

    @property
    def town(self):
        return self.__town

    def __str__(self) -> str:
        return 'Location {' + '\n' + \
               '\t' + 'postCode: ' + self.__postCode + '\n' + \
               '\t' + 'outerCode: ' + self.__outerCode + '\n' + \
               '\t' + 'region: ' + self.__region + '\n' + \
               '\t' + 'town: ' + self.__town + '\n' + \
               '\t' + '}' + '\n'


class Address:
    def __init__(self, address1="", address2="", location=Location):
        self.__address1 = address1
        self.__address2 = address2
        self.__location = location

    @property
    def address1(self):
        return self.__address1

    @property
    def address2(self):
        return self.__address2

    @property
    def location(self):
        return self.__location

    def __str__(self) -> str:
        return 'Address {' + '\n' + \
               '\t' + 'address1: ' + self.__address1 + '\n' + \
               '\t' + 'address2: ' + str(self.__address2) + '\n' + \
               '\t' + '}' + '\n'


class Client:
    def __init__(self, clientID=0, clientName="", clientType="", clientSize="",
                 clientSince=datetime.datetime(1900, 1, 1), address=Address, country=Country, isCreditWorthy=False, isDealer=False):
        self.__clientID = clientID
        self.__clientName = clientName
        self.__clientType = clientType
        self.__clientSize = clientSize
        self.__clientSince = clientSince
        self.__address = address
        self.__country = country
        self.__isCreditWorthy = isCreditWorthy
        self.__isDealer = isDealer

    @property
    def clientID(self):
        return self.__clientID

    @property
    def clientName(self):
        return self.__clientName

    @property
    def clientType(self):
        return self.__clientType

    @property
    def clientSize(self):
        return self.__clientSize

    @property
    def clientSince(self):
        return self.__clientSince

    @property
    def address(self):
        return self.__address

    @property
    def country(self):
        return self.__country

    def isCreditWorthy(self):
        return self.__isCreditWorthy

    def isDealer(self):
        return self.__isDealer

    def __str__(self) -> str:
        return 'Client {' + '\n' + \
               '\t' + 'clientID: ' + str(self.__clientID) + '\n' + \
               '\t' + 'clientName: ' + self.__clientName + '\n' + \
               '\t' + 'clientType: ' + self.__clientType + '\n' + \
               '\t' + 'clientSize: ' + self.__clientSize + '\n' + \
               '\t' + 'clientSince: ' + str(self.__clientSince) + '\n' + \
               '\t' + 'isCreditWorthy: ' + str(self.__isCreditWorthy) + '\n' + \
               '\t' + 'isDealer: ' + str(self.__isDealer) + '\n' + \
               '\t' + '}' + '\n'


class Vehicule:
    def __init__(self, id="", brand="", color="", modelYear=0):
        self.__id = id
        self.__brand = brand
        self.__color = color
        self.__modelYear = modelYear

    @property
    def id(self):
        return self.__id

    @property
    def brand(self):
        return self.__brand

    @property
    def color(self):
        return self.__color

    @property
    def modelYear(self):
        return self.__modelYear

    def __str__(self) -> str:
        return 'Vehicule {' + '\n' + \
               '\t' + 'id: ' + str(self.__id) + '\n' + \
               '\t' + 'brand: ' + self.__brand + '\n' + \
               '\t' + 'color: ' + self.__color + '\n' + \
               '\t' + 'modelYear: ' + str(self.__modelYear) + '\n' + \
               '\t' + '}' + '\n'


class Car(Vehicule):
    def __init__(self, id="", brand="", color="", modelYear=0):
        super().__init__(id, brand, color, modelYear)
        
    def __str__(self) -> str:
        return 'Car {' + '\n' + \
               '\t' + super(Car, self).__str__() + '\n' + \
               '\t' + '}' + '\n'


class Motorycle(Vehicule):
    def __init__(self, id="", brand="", color="", modelYear=0):
        super().__init__(id, brand, color, modelYear)

    def __str__(self) -> str:
        return 'Motorcycle {' + '\n' + \
               '\t' + super(Motorycle, self).__str__() + '\n' + \
               '\t' + '}' + '\n'


class Sale:
    def __init__(self, id=0, year=datetime.datetime(1900, 1, 1), vehicule = Vehicule, client = Client):
        self.__id = id
        self.__year = year
        self.__vehicule = vehicule
        self.__client = client

    @property
    def id(self):
        return self.__Id

    @property
    def year(self):
        return self.__year

    @property
    def vehicule(self):
        return self.__vehicule

    @property
    def client(self):
        return self.__client

    def __str__(self) -> str:
        return 'Sale {' + '\n' + \
               '\t' + str(self.__id) + '\n' + \
               '\t' + str(self.__year) + '\n' + \
               '\t' + self.__vehicule.__str__() + '\n' + \
               '\t' + self.__client.__str__() + '\n' + \
               '\t' + '}' + '\n'


if __name__ == '__main__':
    country = Country(1, "Staffs")
    print(country)
    location = Location("ST17 99RZ", "ST", "East Midlands", "Uttoxeter")
    print(location)
    address = Address("4, Scale Street", None, location)
    print(address)
    client = Client(1, "Aldo Motors", "Wholesaler", "Large", datetime.datetime(1998, 4, 1), False, False)
    print(client)
    car = Car(1, "Toyota", "Blue", 2000)
    print(car)
    motorcycle = Motorycle(1, "Honda", "Red", 1992)
    print(motorcycle)
    sale = Sale(1, datetime.datetime(2008, 1, 1), car, client)
    print(sale)
