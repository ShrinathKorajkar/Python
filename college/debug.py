import traceback, logging

length = input('Enter length : ')
try:
    if length.isdigit() != True:
        raise Exception('Length must be a number')
    else:
        print(length)
except Exception as err:
    print('An Exception occurred : ' + str(err))

# traceback
try:
    raise Exception('This is error msg')
except Exception as err:
    print('this is traceback')
    print(traceback.format_exc())

# Assertion
hello = 'hello'
assert hello == 'hello', 'This is error msg'
hello = 'hel'
assert hello == 'hello', 'This is error msg'

# logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')  #filename can be added
logging.disable(logging.CRITICAL)
logging.debug('Start of program')  #logging.info,warning,error,critical


def fac(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total


print(fac(5))
logging.debug('End of Program')

# Debugging debug check boxes
print('hello')
hey = input()
print(hey)
