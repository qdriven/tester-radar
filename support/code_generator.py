#!/usr/bin/env python
# -*- coding: utf-8 -*-
from jinja2 import Template


def generate_by_templat(template_path:str,context_data:dict)->str:
    with open(template_path,'r') as tmp:
        lines = tmp.readlines()
        template = Template("".join(lines))
        return template.render(context_data)


if __name__ == '__main__':
    # methods = ["_setPendingAdmin","_acceptAdmin",
    #            "_setGlobalParam","_setPriceOracle",
    #            "_setWingAddr","_setCloseFactor",
    #            "_setInsuranceRepayFactor","_setMaxAssets",
    #            "_setLiquidationIncentive","_supportMarket",
    #            "_setPauseGuardian","_setMintPaused","_setBorrowPaused",
    #            "_setTransferPaused","_setSeizePaused","_setWingRate"
    #             ,"_setWingSBLPortion","_updateMarketWingWeight","_addWingMarkets",
    #            "_dropWingMarket","repayByInsurance"]

    methods=["mintAllowed","redeemAllowed","borrowAllowed"
            ,"repayBorrowAllowed","liquidateBorrowAllowed","seizeAllowed",
                  "transferAllowed","assetsIn","checkMembership"
                ,"mintVerify","redeemVerify","borrowVerify",
                  "repayBorrowVerify","liquidateBorrowVerify",
                  "seizeVerify","transferVerify","getAccountLiquidity",
                  "getHypotheticalAccountLiquidity",
                  "liquidateCalculateSeizeTokens",
                  "admin","pendingAdmin","oracle",
                  "closeFactorMantissa",
                  "insuranceRepayFactorMantissa",
                  "couldRepayByInsurance","liquidationIncentiveMantissa"
                    ,"maxAssets","marketMeta","pauseGuardian"
                ,"transferGuardianPaused","seizeGuardianPaused",
                  "mintGuardianPaused","borrowGuardianPaused"
                ,"allMarkets","isMarketExisted"
                ,"wingDistributedNum","wingAddr"
                ,"wingRate","wingSpeeds","wingSBLPortion"
                ,"wingSupplyState","wingBorrowState","wingInsuranceState"
                ,"wingSupplierIndex","wingBorrowerIndex","wingInsuranceIndex"
                ,"wingAccrued","isComptroller"]
    for method in methods:
        data= {"methodNameUpper":method.replace("_","").capitalize(),"methodName":method}
        with open("result.go",'a') as f:
            f.write(generate_by_templat("smartcontractPre.part",data)+"\n")