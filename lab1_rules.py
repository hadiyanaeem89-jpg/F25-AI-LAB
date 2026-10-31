# the new conditions awhich are added are attendance and fee_paid
def scholarship(score, documents_complete,attendance,fee_paid ): 
    if score >= 70 and documents_complete == True and attendance >=70 and fee_paid == True:
         return "Review"
    else: "Hold" 
#  four case test
cases = [
    ("pass", 90, True,79,True),
    ("documents_complete failure", 75 , False ,74, False),
    ("attendance", 86, True, 75, True),
    ("fee_paid", 76, True, 67, False ),
]
for name , score, documents_complete , attendance , fee in cases:
    result =   scholarship(score, documents_complete,attendance, fee )
    
    print  ("score",score,
            "documents_complete", documents_complete,
            "attendance", attendance ,
            "fee_paid", fee, 
            "result",result
          )




 