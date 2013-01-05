import socket
import web
import json

import sys, os,traceback
abspath = os.path.dirname(os.path.abspath(__file__))
#print abspath
if abspath not in sys.path:
	sys.path.append(abspath)
if abspath+'/templates' not in sys.path:
	sys.path.append(abspath+'/templates')

os.chdir(abspath)

render = web.template.render('templates/')

db1=web.database(dbn='postgres',user='postgres',pw='hello',db='semis')

urls = (
	'/', 'index',
	'/go','result'
)

values={"dist":'0'}
queryvalues={"sslccode":"","sslcname":"","semiscode":"","semisname":""}


class prints:
	def GET(SELF):
		return render.prints()

class index:
	def GET(SELF):
			#dists,blcks,clsts,schls=[],[],[],[]
			district = db1.query('select distinct a.district_code as id,a.district_name as name from look_up as a,sslc_data as b,semis_data as c where a.district_code=b.district_code and a.district_name=c.district_name')
			sslc_schools = db1.query('select a.school_code,a.school_name from sslc_data as a,look_up as b where a.district_code=''$dist'' and a.district_code=b.district_code order by school_name',values)
			semis_schools=db1.query('select a.school_code,a.school_name,a.district_name,a.block_name,a.village_name,a.pincode from semis_data as a,look_up as b where b.district_code=''$dist'' and a.district_name=b.district_name order by school_name',values)
			return render.compare(district,values,sslc_schools,semis_schools)
				

application = web.application(urls,globals()).wsgifunc()


class result:
    def POST(self):
	inputs=web.input()
	global values
	if str(inputs.sslc)!='' and str(inputs.semis)!='' and values["dist"]==str(inputs.dist):
		queryvalues["sslccode"]=str(inputs.sslc).split("|")[0]
		queryvalues["sslcname"]=str(inputs.sslc).split("|")[1]
		queryvalues["semiscode"]=str(inputs.semis).split("|")[0]
		queryvalues["semisname"]=str(inputs.semis).split("|")[1]
		db1.query('insert into semis_sslc_match_found values($sslccode,$sslcname,$semiscode,$semisname)',queryvalues)
		db1.query('delete from sslc_data where school_code=trim($sslccode)',queryvalues)
		db1.query('delete from semis_data where school_code=trim($semiscode)',queryvalues)
	values["dist"]=str(inputs.dist)
        raise web.seeother('/')
