ass TickerData():
    """
    Maintans a list of ticker lists
    Defaults to 'tickers.dat'
    Stores each list as one line in a tab seperated text file
    The list's descriptive title is stored in column 1
    """

    def __init__(self, filename = 'tickers.dat', silent=False):
        """
        Initialize ticker lists
        try to load from filename (def = tickers.dat)
        """
        self.indexes = {
            'dow': yfs.tickers_dow,
            'nasdaq': yfs.tickers_nasdaq,
            'sp500': yfs.tickers_sp500}

        filename = os.path.join(os.path.expanduser('~'), filename)
        self.changed = False
        self.silent = silent
        self.ticker_lists = {}
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
        except IOError as err:
            if not silent:
                print('failed to load list data')
            lines = []
        for line in lines:
            if line.strip():
                items = line.strip().split('\t')
                if items[0].lower() not in self.indexes:
                    self.ticker_lists[items[0].lower()] = items[1:]
        else:
            if not silent:
                print('loaded {} stock lists from {}'.format(len(self.ticker_lists), filename))
    def __getitem__(self, index):
        index = index.lower()
        if index in self.indexes:
            return self.indexes[index]()
        elif index in self.ticker_lists:
            return self.ticker_lists[index]
        else:
            return []
    def __exit__(self):
        self.Save()

    def Add(self, tickers):
        """
        Display a prompt for users to select a list
        Add tickers to the selected list
        """
        if tickers:
            self.changed = True
            name = self.get_name().lower()
            if name in self.ticker_lists:
                self.ticker_lists[name] += tickers
                '''
                # now removing dups in the Save method
                self.ticker_lists[name] += [
                    t for t in tickers if t not in self.ticker_lists[name] ]
                '''
            else:
                self.ticker_lists[name] = tickers

    def Filter(self, name, items):
        """
        Remove items from named ticker_list
        """
        self.changed = True
        if name in self.ticker_lists:
            self.ticker_lists[name] = [
                t for t in self.ticker_lists[name] if t not in items]

    def Save(self, filename = 'tickers.dat'):
        """
        Save the ticker lists to filename (def = tickers.dat)
        """
        if not self.changed:
            if not self.silent:
                print('no changes to save')
            return
        filename = os.path.join(os.path.expanduser('~'), filename)
        if not self.silent:
            print('saving {} stock lists to {}'.format(len(self.ticker_lists), filename))
        try:
            with open(filename, 'w') as f:
                for tick_list in self.ticker_lists:
                    items = list(oDict.fromkeys(self.ticker_lists[tick_list])) # remove dups
                    line = '\t'.join(items)
                    if line and tick_list:
                        print(tick_list + '\t' + line, file=f)
        except IOError as err:
            print('failed to save list data')
            
    def get_name(self, new=True, create=False, indexes=True):
        """
        Prompt user to select a list
        show 'New List' at the top of list unless new=False
        """
        choices = list(self.ticker_lists.keys())
        choices = choices + list(self.indexes.keys()) if indexes and not create else choices
        choices = sorted(choices)
        if create:
            choices = ['Select New'] + choices
        elif new:
            choices = ['New List'] + choices

        question = [{
            'type': 'list',
            'name': 'choice',
            'message': 'Select list to add tickers',
            'choices': choices }]
        choice = prompt(question)['choice']
        if choice == 'Select New':
            self.select_tickers()
            return self.get_name(create=True, indexes=False)
        elif choice == 'New List':
            question = [{
                'type': 'input',
                'name': 'input',
                'message': 'List to add tickers to'}]
            return prompt(question)['input']    
        else:
            return choice or 'default'

    def select_tickers(self):
        import ticks
        questions = [
            {
                'type': 'input',
                'name': 'company',
                'message': 'Company search string'},
            {
                'type': 'input',
                'name': 'sector',
                'message': 'Sector search string'},
            {
                'type': 'input',
                'name': 'industry',
                'message': 'Industry search string'} ]
        results = prompt(questions)

        tickers = ticks.SearchTickers(
            exchange_source_dict, results['company'],
            results['sector'], results['industry'])

        print(tickers)
        return True

class CompanyData():
    def __init__(self):
        self.loaded = False

    def retrieve_data(self):
        print('Downloading Company Data')
        exchanges = exchange_source_dict
        #self.company_data = pd.concat(map(pd.read_csv, exchanges.values()))

        dfs = []
        for exchange in exchanges:
            df = pd.read_csv(exchanges[exchange])
            df['Exchange'] = exchange
            dfs.append(df)
        self.company_data = pd.concat(dfs)

        df = self.company_data.filter(items=['Symbol', 'Name', 'Exchange'])
        df.set_index('Symbol', inplace=True)
        self.company_names = df
        self.loaded = True
        print('done')

    def retrieve_data_a(self):
        print('Downloading Company Data')
        exchanges = exchange_source_dict
        #self.company_data = pd.concat(map(pd.read_csv, exchanges.values()))

        dfs = []
        for exchange in exchanges:
            df = pd.read_csv(exchanges[exchange])
            df['Exchange'] = exchange
            dfs.append(df)
        self.company_data = pd.concat(dfs)

        df = self.company_data.filter(items=['Symbol', 'Name', 'Exchange'])
        df.set_index('Symbol', inplace=True)
        self.company_names = df
        self.loaded = True



    def __call__(self):
        if not self.loaded:
            self.retrieve_data()
        return self.company_data

    def GetNames(self, tickers):
        if not self.loaded:
            self.retrieve_data()

        df = self.company_names.loc[tickers]
        return df

    def GetData(self, exchanges=None):
        if not self.loaded:
            self.retrieve_data()
        df = self.company_data
        if exchanges:
            df = df[df.Exchange.isin(exchanges)]
        return df.filter(items=['Symbol', 'Name', 'Sector', 'industry'])
