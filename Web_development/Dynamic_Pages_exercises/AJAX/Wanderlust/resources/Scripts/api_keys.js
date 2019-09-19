const keys = {
  // Foursquare keys
  _FSClientId: '?client_id=TVQY3VI0O33HA04DH0UO2YTJYN1TKFBZWBFMHLGXFDRAQHYQ',
  _FSSecret: '&client_secret=IWVW0YYAHZRB4OULZNLH30XZIB1RT1I5ZCZMLWT4A1QD1P3H',

  // APIXU keys
  _APIXUKey: '?access_key=513259d0f64449c4e2603e91a2387fb8',

  get FSClientId () {
    return this._FSClientId
  },
  get FSSecret () {
    return this._FSSecret
  },
  get APIXUKey () {
    return this._APIXUKey
  }
}
export default keys
