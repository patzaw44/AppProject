from modul3 import inna_funkcja
import faker

fake = faker.Faker('pl_PL')


def wygeneruj_osobe():
    return {
        "imie":fake.first_name(),
        "nazwisko":fake.last_name()

    }


if __name__ == "__main__":
    print(wygeneruj_osobe())
    inna_funkcja()
