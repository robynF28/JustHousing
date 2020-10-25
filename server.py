from flask import Flask, jsonify, request, render_template, abort, session, send_from_directory, url_for, send_file
import flask
import io

#import Address
from fairpricecalc import FairPriceCheck
from textsummary import AutomaticSummarization



app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/get_address_info", methods=["GET"])
def get_address_info():

    address = request.args.get("address")
    zipcode = request.args.get("zipcode")
    print(address)
    print(zipcode)
    
    #blah = Address()
    #user_info = request.get_json(force=True)


    temp = FairPriceCheck(address, zipcode)

    #result = blah.function_name()

    #return jsonify({"hi" : result})
    print(temp.return_fair())
    return jsonify({"The pricing is fair if a 0, overpriced if a 1" : temp.return_fair()})

@app.route("/get_contract_info", methods=["GET"])
def get_contract_info():

    contract = request.args.get("contract")
    with open("autosum.txt","w", encoding="utf-8") as text_file:
        text_file.write(contract)
    text_file.close()
    summarization = AutomaticSummarization()
    print(str(summarization.return_sentence))
    #return jsonify({})
    return jsonify({"Your contract decoded" : str(summarization.return_sentence())})
    


#@app.route("/get_address_info", methods=["POST"])
#def get_address_info():
#    
#    #blah = Address()
#    user_info = request.get_json(force=True)
#
#    temp = FairPriceCheck(user_info["address"], user_info["zipcode"])

#    #result = blah.function_name()

#    #return jsonify({"hi" : result})
#    return jsonify({"hi" : temp.return_fair})

@app.route("/")
def main():
    return render_template('main.html')

if __name__ == "__main__":
    app.run()