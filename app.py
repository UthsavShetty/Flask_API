try:
    from API import (app,
                     api,
                     Controller,
                     HouseLookupController)

except Exception as e:
    print("Modules are Missing : {} ".format(e))


api.add_resource(Controller, '/houseprice')
api.add_resource(HouseLookupController, '/houselookup')


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
