def main():
    Total=0
    count=1
    print("Enter marks according to sequence in integer form. Once marks is done type complete.")
    while True:
        try:
            marks=input(f"Enter marks of {count} subject:").lower()
            if marks == "complete":
                raise ValueError("completed")
            else:
                marks=int(marks)
            if marks<0 or marks>100:
               raise ValueError("Invalid input")
        except ValueError as e:
            if str(e) == "Invalid input":
                print("Marks should be under 100 and above 0.")
            elif str(e) == "completed":
                break
            else:
                print("Enter Integer value.")
        else:
            total+=marks
            count+=1
    actual_subject_count = count - 1
    if actual_subject_count > 0:
        x = percent(total, actual_subject_count) 
        print(f"Percentage is {x:.2f}%")
    else:
        print("No marks were entered. Cannot calculate percentage."))

def percent(total,count):
    return total/count

main()
