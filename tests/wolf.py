import wolframalpha


client = wolframalpha.Client("544R9X-8R9Y6QAR4R")
res = client.query('temperature in Washington, DC on October 3, 2012')
print(next(res.results).text)
