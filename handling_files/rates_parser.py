import json

class RatesParser:
    def __init__(self, rates_filepath):
        rates_info = self._open_json_file(rates_filepath)
        self.base = rates_info["base"]
        self.date = rates_info["date"]
        self.aud = rates_info["rates"]["AUD"]
        self.gbp = rates_info["rates"]["GBP"]
        self.usd = rates_info["rates"]["USD"]

    def _open_json_file(self, filepath) -> dict:
        with open(filepath) as rates:
            return json.load(rates) 


rp = RatesParser('exchange_rates.json')
rates_info = rp._open_json_file('exchange_rates.json')
print(rp.gbp)
print(rates_info)