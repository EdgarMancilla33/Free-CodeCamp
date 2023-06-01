import struct

def main():

    record_format = struct.Struct("30s f")
    with open("data.bin", "wb") as file:

        file.write(record_format.pack (b"Juan Fernandez", 3.7))
        file.write(record_format.pack (b"Alejandro Contreras", 4.2)) 
        file.write(record_format.pack (b"Patricia Figueroa", 5.8))

    with open("data.bin", "rb") as file:

        while True:
            record = file.read(record_format.size)
            if not record:
                break

            name, average = record_format.unpack (record)

            print("Name:", name.decode().strip(), "average: ", average)

if __name__ == "__main__":

    main()