LOGIN_CONFIRMATION = "MATCH (s:Student {ID: $stud_id})-[:LIVES_IN]->(r:Room)-[:PART_OF]->(w:Wing)-[:PART_OF_2]->(h:Hostel) RETURN s, r, h"
SHOW_CURRENT_PREFERENCES = "MATCH (s:Student {ID: $stud_id}) -[pr:PREFERS]->(pref:Preference) RETURN pref"
# CREATE_PREFERENCE
FIND_1_SWAP = """MATCH (you:Student {ID: $stud_id})-[:PREFERS]->(pref:Preference)
MATCH (s:Student)-[:LIVES_IN]->(r:Room)-[:PART_OF]->(w:Wing)-[:PART_OF_2]->(h:Hostel)
WHERE s.OpenToSwap = true AND pref.Hostel = h.Name AND r.Number >= pref.minRoom AND r.Number <= pref.maxRoom AND w.WesternToilets >= pref.minWesternToilets
RETURN r, s"""

