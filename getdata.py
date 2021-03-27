import twint

from datetime import datetime

def lastminute(keyword):
    oneminuteago = datetime.today().strftime('%Y-%m-%d %H:') + str(int(datetime.today().strftime('%M'))-1)+ datetime.today().strftime(':%S')
    c = twint.Config()
    c.Search = keyword
    c.Until = oneminuteago
    c.Output = 'result.csv'
    c.Hide_output = True
    c.Count = True

    twint.run.Search(c)

    count = 0

    with open("result.csv", encoding = 'utf8') as file:
        count = sum(1 for line in file)
    
    
    print(count)

lastminute('dogecoin')


