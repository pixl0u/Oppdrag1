from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

sted='film'
tittel='film'
img=''
text='film text'
pris = 0

@app.route("/endre_sted")
def endre_sted():
    global sted
    global tittel
    global img
    global text
    global pris
    sted = "Clayface"
    tittel = 'Clayface'
    img = '/static/img/Clayface.png'
    text = 'Matt Hagens reise fra gategutt til hollywoodstjerne er nær ved å fullendes, når en av Gothams mafiosoer ødelegger alt ved å vansire ham. Alene og uten mer å tape, oppsøker Matt hjelp gjennom en banebrytende behandling som gir ham sitt gamle jeg tilbake... Samtidig som det uventet påvirker hans grep om virkeligheten, noe som leder ham ut på en ferd drevet av altoppslukende hevn.'
    pris = 299
    return redirect(url_for("bilett"))

@app.route("/endre_sted1")
def endre_sted1():
    global sted
    global tittel
    global img
    global text
    global pris
    pris = 349
    sted='Street fighter'
    tittel='Street fighter'
    img='/static/img/Street-Fighter.png'
    text='Street Fighter-utøverne Ryu og Ken Masters var som brødre, men har ikke snakket sammen på årevis etter en hendelse som rev vennskapet i stykker. Ut av det blå blir de begge rekruttert av den mystiske Chun-Li til et verdensmesterskap i kampsporten de har felles. Konkurransen presenteres som en legendarisk begivenhet man ikke kan si nei til, men bak turneringen skjuler det seg en farlig konspirasjon med katastrofale konsekvenser. Ryu og Ken må legge rivaliseringen til side for å takle deres livs største utfordring.'
    return redirect(url_for("bilett"))

@app.route("/endre_sted2")
def endre_sted2():
    global sted
    global tittel
    global img
    global text
    global pris
    pris = 150
    sted = "Verity"
    tittel='Verity'
    img='/static/img/Verity.png'
    text='Vi møter den anerkjente forfatteren Verity Crawford og Lowen Ashleigh, en presset forfatter som flytter til den avsidesliggende Crawford-eiendommen for å ghostwrite for Verity. Når Lowen oppdager det som ser ut til å være Veritys urovekkende selvbiografiske notater, blir hun dratt inn i mørke og forvridde bekjennelser om Veritys ektemann Jeremy. I takt med at grensene viskes ut, kjemper hun med å skille fiksjon fra virkelighet, manipulasjon fra tiltrekning, og mulighet fra besettelse.'
    return redirect(url_for("bilett"))

@app.route("/endre_sted3")
def endre_sted3():
    global sted
    global tittel
    global img
    global text
    global pris
    pris = 120
    sted = "Digger"
    tittel='Digger'
    img='/static/img/Digger.png'
    text='Den mektigste mannen i verden legger ut på et panisk oppdrag for å bevise at han er menneskehetens redningsmann før katastrofen han selv har utløst ødelegger alt.'
    return redirect(url_for("bilett"))

@app.route("/endre_sted4")
def endre_sted4():
    global sted
    global tittel
    global img
    global text
    global pris
    pris = 499
    sted = "Spider-Man: Brand New Day"
    tittel='Spider-Man: Brand New Day'
    img='/static/img/Spider-Man-Brand–New-Day.png'
    text='Det har gått fire år siden hendelsene i No Way Home. Peter er nå voksen og lever alene, etter at han frivillig slettet seg selv fra livene og minnene til dem han elsker. I et New York som ikke lenger vet hvem han er, har han viet seg til å beskytte byen som Spider-Man på heltid. Men etter hvert som kravene til ham øker, utløser presset en uventet fysisk utvikling som truer hans eksistens. Samtidig danner et mystisk nytt mønster av forbrytelser grunnlaget for en av de farligste truslene han noen gang har stått overfor.'
    return redirect(url_for("bilett"))

@app.route("/endre_sted5")
def endre_sted5():
    global sted
    global tittel
    global img
    global text
    global pris
    pris = 189
    sted = "Lille spøkelset Laban skøyer igjen"
    tittel='Lille spøkelset Laban skøyer igjen'
    img='/static/img/Lille-spøkelset-Laban-skøyer-igjen.png'
    text='Lille spøkelset Laban er tilbake med en ny samling koselige og passe skumle eventyr på Godmorgen solslott. Sammen med lillesøster Labolina og bestevennen Lilleprins Bus byr dagene på alt fra knask eller knep, bursdagsfeiring og bortkomne julegaver til uventede gjester og mange andre morsomme opplevelser. En sjarmerende kinofilm fylt med lek, latter og spøk for de aller minste.'
    return redirect(url_for("bilett"))


@app.route("/")
def index():
    global sted
    return render_template("index.html")

@app.route("/bilett", methods=["GET", "POST"])
def bilett():
    global sted
    global tittel
    global img
    global text
    global pris
    side='2'
    filmer=['Clayface','Street Fighter','Verity','Digger','Spider-Man: Brand New Day','Lille spøkelset Laban skøyer igjen']
    filmer.insert(0,sted)
    if request.method == "POST":
        navn = request.form["navn"]
        sete = request.form["sete"]
        antall = int(request.form["antall"])
        film = request.form["film"]
        pris=pris*antall
        return render_template("ferdig.html",navn=navn,sete=sete,antall=antall,film=film,pris=pris)
    return render_template('bilett.html',filmer=filmer,sted=sted,tittel=tittel,img=img,text=text,pris=pris)


@app.route("/ferdig")
def ferdig():
    global sted
    return render_template("index.html")


@app.route("/om_oss")
def om_oss():
    return render_template("om_oss.html")

if __name__ == "__main__":
    app.run(debug=True)