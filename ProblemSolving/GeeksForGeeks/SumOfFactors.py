# Sum of all the divisors of a number
def sum_of_Div(number):
    divisors  = [1]
    for i in range(2, number+1):
        if(number%i) == 0:

            divisors.append(i)
    return divisors
print(sum_of_Div(30))
print(sum(sum_of_Div(30)))
