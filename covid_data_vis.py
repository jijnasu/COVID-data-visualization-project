"""
The program visualizes the COVID data of the country entered by the user...
"""
# https://github.com/CSSEGISandData/COVID-19

import matplotlib.pyplot as plt

def main():
    opt='0'
    while opt!='':
        opt = input("Enter country name to continue(else Enter) : ")
        country = opt
        country_path = 'countries/'+country+'.txt'
        try:
            open(country_path)
        except:
            if opt=='':
                print("Thank you :)< ")
            else:
                print("Please retry...")
            continue
        # Extracting data of the country entered by the user
        cases,new_cases,days = extract_data(country_path)
        # Plotting and showing the data using graphs
        plot_graph(cases,new_cases,days,country)


def extract_data(country_path):
    """
    The function loads data of the country entered and returns the lists of 
    total # of cases in each day, # of new cases in each day and # of days from Jan 22nd, 2020.
    """
    with open(country_path) as f:
        data = f.read()
        data = list(data.split('\n'))
        cases = list(map(lambda x:int(x),data))
        new_cases = list(cases[i]-cases[i-1] for i in range(1,len(cases)))
        new_cases = [cases[0]] + new_cases
        days=list(range(1,len(cases)+1))
    return cases,new_cases,days
        
def plot_graph(cases,new_cases,days,country):
    """
    The function plots two subplots 
    1--> total cases VS days 
    2--> new cases VS days 
    """
    plt.close()
    # plt.style.context('dark_background')
    # plt.style.use('dark_background')
    plt.style.use('ggplot')
    plt.figure(figsize=(15,10), dpi=100)
    plt.subplot(211)
    plt.title('COVID-19 Cases in '+country.upper())
    plt.plot(days,cases,'r')
    plt.xlabel('No. of days starting from Jan 22nd, 2020')
    plt.ylabel("No. of cases")
    plt.subplot(212)
    plt.plot(days,new_cases,'g')
    plt.xlabel('No. of days starting from Jan 22nd, 2020')
    plt.ylabel("No. of new-cases/day")
    plt.show()
    plt.close()



if __name__ == '__main__':
    main()
