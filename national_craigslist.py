'''
Name    John Park
Github  john-yohan-park
Date    12/23/2019
'''

from selenium                      import webdriver        # interact with browser to scrape
from selenium.webdriver.support.ui import WebDriverWait    # wait for page to load
from selenium.webdriver.support    import expected_conditions as EC # check element is present in HTML
from selenium.webdriver.common.by  import By               # find element by id
from selenium.common.exceptions    import TimeoutException # exit if page takes too long to load
from bs4                           import BeautifulSoup    # parse HTML once scraped
from urllib                        import request          # open URL
from sys                           import argv             # get command line arguments
import ssl                                                 # create secure client-server connection

class CL_scraper(object):
    def __init__(self, item, min_price, max_price): # initialize instance variables
        self.item      = item.replace(' ', '+')     # url plug-able item name
        self.min_price = min_price                  # min price willing to pay for item
        self.max_price = max_price                  # max price willing to pay for item
        self.driver    = webdriver.Firefox()        # instantiate web session

    def search(self):
        # custom US cities to search
        # self.cities = ['losangeles', 'newyork', 'chicago']
        
        # list of US cities that have unique Craigslist url
        self.cities = ['auburn', 'bham', 'dothan', 'shoals', 'gadsden', 'huntsville', 'mobile', 'montgomery', 'tuscaloosa', 'anchorage', 'fairbanks', 'kenai', 'juneau', 'flagstaff', 'mohave', 'phoenix', 'prescott', 'showlow', 'sierravista', 'tucson', 'yuma', 'fayar', 'fortsmith', 'jonesboro', 'littlerock', 'texarkana', 'bakersfield', 'chico', 'fresno', 'goldcountry', 'hanford', 'humboldt', 'imperial', 'inlandempire', 'losangeles', 'mendocino', 'merced', 'modesto', 'monterey', 'orangecounty', 'palmsprings', 'redding', 'sacramento', 'sandiego', 'sfbay', 'slo', 'santabarbara', 'santamaria', 'siskiyou', 'stockton', 'susanville', 'ventura', 'visalia', 'yubasutter', 'boulder', 'cosprings', 'denver', 'eastco', 'fortcollins', 'rockies', 'pueblo', 'westslope', 'newlondon', 'hartford', 'newhaven', 'nwct', 'delaware', 'washingtondc', 'miami', 'daytona', 'keys', 'fortlauderdale', 'fortmyers', 'gainesville', 'cfl', 'jacksonville', 'lakeland', 'lakecity', 'ocala', 'okaloosa', 'orlando', 'panamacity', 'pensacola', 'sarasota', 'spacecoast', 'staugustine', 'tallahassee', 'tampa', 'treasure', 'albanyga', 'athensga', 'atlanta', 'augusta', 'brunswick', 'columbusga', 'macon', 'nwga', 'savannah', 'statesboro', 'valdosta', 'honolulu', 'boise', 'eastidaho', 'lewiston', 'twinfalls', 'bn', 'chambana', 'chicago', 'decatur', 'lasalle', 'mattoon', 'peoria', 'rockford', 'carbondale', 'springfieldil', 'quincy', 'bloomington', 'evansville', 'fortwayne', 'indianapolis', 'kokomo', 'tippecanoe', 'muncie', 'richmondin', 'southbend', 'terrehaute', 'ames', 'cedarrapids', 'desmoines', 'dubuque', 'fortdodge', 'iowacity', 'masoncity', 'quadcities', 'siouxcity', 'ottumwa', 'waterloo', 'lawrence', 'ksu', 'nwks', 'salina', 'seks', 'swks', 'topeka', 'wichita', 'bgky', 'eastky', 'lexington', 'louisville', 'owensboro', 'westky', 'batonrouge', 'cenla', 'houma', 'lafayette', 'lakecharles', 'monroe', 'neworleans', 'shreveport', 'maine', 'annapolis', 'baltimore', 'easternshore', 'frederick', 'smd', 'westmd', 'boston', 'capecod', 'southcoast', 'westernmass', 'worcester', 'annarbor', 'battlecreek', 'centralmich', 'detroit', 'flint', 'grandrapids', 'holland', 'jxn', 'kalamazoo', 'lansing', 'monroemi', 'muskegon', 'nmi', 'porthuron', 'saginaw', 'swmi', 'thumb', 'up', 'bemidji', 'brainerd', 'duluth', 'mankato', 'minneapolis', 'rmn', 'marshall', 'stcloud', 'gulfport', 'hattiesburg', 'jackson', 'meridian', 'northmiss', 'natchez', 'columbiamo', 'joplin', 'kansascity', 'kirksville', 'loz', 'semo', 'springfield', 'stjoseph', 'stlouis', 'billings', 'bozeman', 'butte', 'greatfalls', 'helena', 'kalispell', 'missoula', 'montana', 'grandisland', 'lincoln', 'northplatte', 'omaha', 'scottsbluff', 'elko', 'lasvegas', 'reno', 'nh', 'cnj', 'jerseyshore', 'newjersey', 'southjersey', 'albuquerque', 'clovis', 'farmington', 'lascruces', 'roswell', 'santafe', 'albany', 'binghamton', 'buffalo', 'catskills', 'chautauqua', 'elmira', 'fingerlakes', 'glensfalls', 'hudsonvalley', 'ithaca', 'longisland', 'newyork', 'oneonta', 'plattsburgh', 'potsdam', 'rochester', 'syracuse', 'twintiers', 'utica', 'watertown', 'asheville', 'boone', 'charlotte', 'eastnc', 'fayetteville', 'greensboro', 'hickory', 'onslow', 'outerbanks', 'raleigh', 'wilmington', 'winstonsalem', 'bismarck', 'fargo', 'grandforks', 'nd', 'akroncanton', 'ashtabula', 'athensohio', 'chillicothe', 'cincinnati', 'cleveland', 'columbus', 'dayton', 'limaohio', 'mansfield', 'sandusky', 'toledo', 'tuscarawas', 'youngstown', 'zanesville', 'lawton', 'enid', 'oklahomacity', 'stillwater', 'tulsa', 'bend', 'corvallis', 'eastoregon', 'eugene', 'klamath', 'medford', 'oregoncoast', 'portland', 'roseburg', 'salem', 'altoona', 'chambersburg', 'erie', 'harrisburg', 'lancaster', 'allentown', 'meadville', 'philadelphia', 'pittsburgh', 'poconos', 'reading', 'scranton', 'pennstate', 'williamsport', 'york', 'providence', 'charleston', 'columbia', 'florencesc', 'greenville', 'hiltonhead', 'myrtlebeach', 'nesd', 'csd', 'rapidcity', 'siouxfalls', 'sd', 'chattanooga', 'clarksville', 'cookeville', 'jacksontn', 'knoxville', 'memphis', 'nashville', 'tricities', 'abilene', 'amarillo', 'austin', 'beaumont', 'brownsville', 'collegestation', 'corpuschristi', 'dallas', 'nacogdoches', 'delrio', 'elpaso', 'galveston', 'houston', 'killeen', 'laredo', 'lubbock', 'mcallen', 'odessa', 'sanangelo', 'sanantonio', 'sanmarcos', 'bigbend', 'texoma', 'easttexas', 'victoriatx', 'waco', 'wichitafalls', 'logan', 'ogden', 'provo', 'saltlakecity', 'stgeorge', 'vermont', 'charlottesville', 'danville', 'fredericksburg', 'norfolk', 'harrisonburg', 'lynchburg', 'blacksburg', 'richmond', 'roanoke', 'swva', 'winchester', 'bellingham', 'kpr', 'moseslake', 'olympic', 'pullman', 'seattle', 'skagit', 'spokane', 'wenatchee', 'yakima', 'charlestonwv', 'martinsburg', 'huntington', 'morgantown', 'wheeling', 'parkersburg', 'swv', 'wv', 'appleton', 'eauclaire', 'greenbay', 'janesville', 'racine', 'lacrosse', 'madison', 'milwaukee', 'northernwi', 'sheboygan', 'wausau', 'wyoming', 'micronesia', 'puertorico', 'virgin']
        
        self.urls   = set()            # set of urls
        print('Searching', end=' ', flush=True)
        for city in self.cities:       # for every city in cities
            self.print_city_name(city) # print city name
            self.label = 'pagenum'     # define label for number of results
            self.load_url(city)        # load Craigslist URL for that city
            self.wait()                # wait till 'pagenum' label appears
            result = self.driver.find_element_by_class_name(self.label) # get 'pagenum' value
            if result.text=='no results': continue # if there are no results, skip to nxt city
            self.add_urls()            # if there are results, add urls

    def print_city_name(self, city): 
        if city==self.cities[-1]:      # if city is last city
            print(city.capitalize())   # print city + '\n'
        else:                          # if city is NOT last city
            print(city.capitalize(), end=', ', flush=True)  # print city + ', '
    
    def load_url(self, city):          # load url with specified city, item, min_price, max_price
        self.url = f'https://{city}.craigslist.org/search/sss?query={self.item}&sort=rel&srchType=T&hasPic=1&min_price={self.min_price}&max_price={self.max_price}'
        self.driver.get(self.url)      # open browser with specified url

    def wait(self):                    # wait 3 sec or until class_name label_to_find appears
        try: WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, self.label)))
        except TimeoutException: print('Could not find ' + self.label) # print if takes too long
    
    def add_urls(self):
        gcontext = ssl.SSLContext()    # bypass SSL Certificate Verification
        html_page = request.urlopen(self.url, context=gcontext) # extract HTML content
        soup = BeautifulSoup(html_page, 'lxml') # pour content into soup obj
        for link in soup.findAll('a', {'class': 'result-title hdrlnk'}): # find tags with <a class='result-title hdrlnk' ...
            self.urls.add(link['href']) # add link

    def print_results(self):
        print()
        if len(self.urls)==0:         # if result is empty, 
            print('No result found.') # print msg
        else:                         # if result is NOT empty,
            for url in self.urls: print(url) # print every url
        print()

    def quit(self):
        self.driver.quit()  # close browser

# capture arguments
item      = argv[1]
min_price = argv[2]
max_price = argv[3]

# use CL_scraper
scraper = CL_scraper(item, min_price, max_price)
scraper.search()
scraper.print_results()
scraper.quit()
