import api_conector
import db


#api_conector.matches.scheduleMatch(fase='final')
#print(api_conector.matches.getMatchesData())
#api_conector.matches.deleteMatch("665c7c270b23098f11fe94b9")

print(db.queries.getAthelets(athelet_id="665b569e3c8033cad08e40e3"))
print(db.queries.getAthelets('brasil'))
print(db.queries.getAthelets())