from flask import Flask, render_template, request, redirect, session, url_for, flash

Harmony = Flask(__name__)
Harmony.secret_key = "SECRET KEY"


@Harmony.route('/')
def root():
        return render_template('3Harmony.html')

@Harmony.route('/play')
def play():
        return render_template('play.html')

@Harmony.route('/about')
def about():
        return render_template('about.html')

@Harmony.route('/results')
def results():
        
        s=0
        d=0
        c=0
        n=0
        
        results = request.args["question1"]
        if( results == "choice1" ):
                s+=1
        if( results == "choice2" ):
                d+=1
        if( results == "choice3" ):
                c+=1
        if( results == "choice4" ):
                n+=1

        results = request.args["question2"]
        if( results == "choice5" ):
                n+=1
        if( results == "choice6" ):
                s+=1
        if( results == "choice7" ):
                c+=1
        if( results == "choice8" ):
                d+=1

        results = request.args["question3"]
        if( results == "choice9" ):
                c+=1
        if( results == "choice10" ):
                n+=1
        if( results == "choice11" ):
                s+=1
        if( results == "choice12" ):
                d+=1

        results = request.args["question4"]
        if( results == "choice13" ):
                d+=1
        if( results == "choice14" ):
                c+=1
        if( results == "choice15" ):
                s+=1
        if( results == "choice16" ):
                n+=1

        results = request.args["question5"]
        if( results == "choice17" ):
                n+=1
        if( results == "choice18" ):
                c+=1
        if( results == "choice19" ):
                s+=1
        if( results == "choice20" ):
                d+=1

        results = request.args["question6"]
        if( results == "choice21" ):
                n+=1
        if( results == "choice22" ):
                s+=1
        if( results == "choice23" ):
                c+=1
        if( results == "choice24" ):
                d+=1
                
        results = request.args["question7"]
        if( results == "choice25" ):
                s+=1
        if( results == "choice26" ):
                c+=1
        if( results == "choice27" ):
                d+=1
        if( results == "choice28" ):
                n+=1

        results = request.args["question8"]
        if( results == "choice29" ):
                d+=1
        if( results == "choice30" ):
                s+=1
        if( results == "choice31" ):
                n+=1
        if( results == "choice32" ):
                c+=1

        results = request.args["question9"]
        if( results == "choice33" ):
                c+=1
        if( results == "choice34" ):
                n+=1
        if( results == "choice35" ):
                s+=1
        if( results == "choice36" ):
                d+=1

        results = request.args["question10"]
        if( results == "choice37" ):
                d+=1
        if( results == "choice38" ):
                c+=1
        if( results == "choice39" ):
                s+=1
        if( results == "choice40" ):
                n+=1

        print "s: " + str(s)
        print "d: " + str(d)
        print "n: " + str(n)
        print "c: " + str(c)
        
        if( s > n ):
                if( s > d ):
                        if( s > c ):
                                most = "Sang"
                        else:
                                most = "Changhoon"
                elif( s > c ):
                        if( s > d ):
                                most = "Sang"
                        else:
                                most = "Devon"
                elif( c > d ):
                        most = "Changhoon"
                else:
                        most = "Devon"
        elif( s > c ):
                if( s > d ):
                        most = "Nina"
                elif( d > n ):
                        most = "Devon"
                else:
                        most = "Nina"
        elif( s > d ):
                if( c > n ):
                        most = "Changhoon"
                else:
                        most = "Nina"
        elif( c > n ):
                if( c > d ):
                        most = "Changhoon"
                else:
                        most = "Devon"
        elif( c > d ):
                most = "Nina"
        elif( n > d ):
                most = "Nina"
        else:
                most = "Devon"
                
        return render_template('results.html', person = most )

if __name__ == '__main__':
        Harmony.debug = True
        Harmony.run()
