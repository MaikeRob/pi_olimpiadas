import api_conector
import db

#api_conector.matches.scheduleMatch(fase='final')
print(api_conector.matches.getMatchesData())
api_conector.matches.deleteMatch("665c7c270b23098f11fe94b9")