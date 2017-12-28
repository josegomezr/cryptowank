import re
import operator

def normalize_ticker_poloniex(poloniex_response):
    normalized = {}
    for currency_pair, currency_object in poloniex_response.items():
        pair = currency_pair.lower()
        currency_object['currencyPair'] = pair
        currency_object['last'] = float(currency_object['last'])
        normalized[pair] = currency_object
    return normalized

VALID_OPS = {
    '>=': operator.ge,
    '<=': operator.le,
    '<': operator.lt,
    '>': operator.gt,
    '=': operator.eq,
}


def parse_rules(rule_list):
    rules = []
    for rule in rule_list:
        rule_tuple = re.split(r'\s+', rule)
        if len(rule_tuple) != 3:
            raise Exception("Couldn't parse rule: '{}'\nWrong number of params".format(rule))
        
        market, operator, target = rule_tuple
        if operator not in VALID_OPS.keys():
            raise Exception("Couldn't parse rule: '{}'\nInvalid operator".format(rule))
        
        target = float(target)

        rules.append({
            'market': market,
            'operator': VALID_OPS[operator],
            'target': target
        })

    return rules
