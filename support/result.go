func(self *CmpControllReader) Mintallowed(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"mintAllowed",params)
}
func(self *CmpControllReader) Redeemallowed(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"redeemAllowed",params)
}
func(self *CmpControllReader) Borrowallowed(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"borrowAllowed",params)
}
func(self *CmpControllReader) Repayborrowallowed(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"repayBorrowAllowed",params)
}
func(self *CmpControllReader) Liquidateborrowallowed(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"liquidateBorrowAllowed",params)
}
func(self *CmpControllReader) Seizeallowed(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"seizeAllowed",params)
}
func(self *CmpControllReader) Transferallowed(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"transferAllowed",params)
}
func(self *CmpControllReader) Assetsin(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"assetsIn",params)
}
func(self *CmpControllReader) Checkmembership(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"checkMembership",params)
}
func(self *CmpControllReader) Mintverify(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"mintVerify",params)
}
func(self *CmpControllReader) Redeemverify(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"redeemVerify",params)
}
func(self *CmpControllReader) Borrowverify(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"borrowVerify",params)
}
func(self *CmpControllReader) Repayborrowverify(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"repayBorrowVerify",params)
}
func(self *CmpControllReader) Liquidateborrowverify(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"liquidateBorrowVerify",params)
}
func(self *CmpControllReader) Seizeverify(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"seizeVerify",params)
}
func(self *CmpControllReader) Transferverify(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"transferVerify",params)
}
func(self *CmpControllReader) Getaccountliquidity(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"getAccountLiquidity",params)
}
func(self *CmpControllReader) Gethypotheticalaccountliquidity(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"getHypotheticalAccountLiquidity",params)
}
func(self *CmpControllReader) Liquidatecalculateseizetokens(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"liquidateCalculateSeizeTokens",params)
}
func(self *CmpControllReader) Admin(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"admin",params)
}
func(self *CmpControllReader) Pendingadmin(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"pendingAdmin",params)
}
func(self *CmpControllReader) Oracle(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"oracle",params)
}
func(self *CmpControllReader) Closefactormantissa(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"closeFactorMantissa",params)
}
func(self *CmpControllReader) Insurancerepayfactormantissa(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"insuranceRepayFactorMantissa",params)
}
func(self *CmpControllReader) Couldrepaybyinsurance(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"couldRepayByInsurance",params)
}
func(self *CmpControllReader) Liquidationincentivemantissa(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"liquidationIncentiveMantissa",params)
}
func(self *CmpControllReader) Maxassets(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"maxAssets",params)
}
func(self *CmpControllReader) Marketmeta(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"marketMeta",params)
}
func(self *CmpControllReader) Pauseguardian(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"pauseGuardian",params)
}
func(self *CmpControllReader) Transferguardianpaused(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"transferGuardianPaused",params)
}
func(self *CmpControllReader) Seizeguardianpaused(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"seizeGuardianPaused",params)
}
func(self *CmpControllReader) Mintguardianpaused(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"mintGuardianPaused",params)
}
func(self *CmpControllReader) Borrowguardianpaused(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"borrowGuardianPaused",params)
}
func(self *CmpControllReader) Allmarkets(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"allMarkets",params)
}
func(self *CmpControllReader) Ismarketexisted(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"isMarketExisted",params)
}
func(self *CmpControllReader) Wingdistributednum(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"wingDistributedNum",params)
}
func(self *CmpControllReader) Wingaddr(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"wingAddr",params)
}
func(self *CmpControllReader) Wingrate(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"wingRate",params)
}
func(self *CmpControllReader) Wingspeeds(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"wingSpeeds",params)
}
func(self *CmpControllReader) Wingsblportion(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"wingSBLPortion",params)
}
func(self *CmpControllReader) Wingsupplystate(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"wingSupplyState",params)
}
func(self *CmpControllReader) Wingborrowstate(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"wingBorrowState",params)
}
func(self *CmpControllReader) Winginsurancestate(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"wingInsuranceState",params)
}
func(self *CmpControllReader) Wingsupplierindex(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"wingSupplierIndex",params)
}
func(self *CmpControllReader) Wingborrowerindex(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"wingBorrowerIndex",params)
}
func(self *CmpControllReader) Winginsuranceindex(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"wingInsuranceIndex",params)
}
func(self *CmpControllReader) Wingaccrued(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"wingAccrued",params)
}
func(self *CmpControllReader) Iscomptroller(contractAddrHex,addrHex string){
	addrx, _ := utils.AddressFromHexString(addrHex)
	params := []interface{}{adminAddr}
	self.SendPreExecuteTx(contractAddrHex,"isComptroller",params)
}
