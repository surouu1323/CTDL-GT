
def calculate_average_temperature(num_of_days, temperatures):
    # Tính trung bình nhiệt độ
    average_temperature = sum(temperatures) / num_of_days

    # Đếm số ngày có nhiệt độ cao hơn trung bình
    above_average_count = sum(1 for temp in temperatures if temp > average_temperature)

    return average_temperature, above_average_count

def main():
    # Nhập số ngày
    num_of_days = int(input("How many day's temperature? "))

    # Nhập nhiệt độ cho mỗi ngày
    temperatures = [float(input(f"Day {i + 1}'s high temp: ")) for i in range(num_of_days)]

    # Tính toán và in kết quả
    average_temperature, above_average_count = calculate_average_temperature(num_of_days, temperatures)
    print(f"\nAverage = {average_temperature}")
    print(f"{above_average_count} day(s) above average")

if __name__ == "__main__":
    main()