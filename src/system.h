/******************** ORBIT.H **********************/
/*
 * Rory Barnes, Wed May  7 13:48:54 PDT 2014
 *
 * This header file contains all the subroutines in
 * file orbit.c.
 *
*/

double fdSemiToPeriod(double,double);
double fdPeriodToSemi(double,double);
double fdSemiToMeanMotion(double,double);
double fdMeanMotionToSemi(double,double,double);
double fdMeanMotionToSemi(double,double,double);

double * fdOrbAngMom(BODY*,CONTROL*,int);
double fdTotAngMom(BODY*,CONTROL*,SYSTEM*);

double fdOrbPotEnergy(BODY*,CONTROL*,SYSTEM*,int);
double fdOrbKinEnergy(BODY*,CONTROL*,SYSTEM*,int);
double fdOrbEnergy(BODY*,CONTROL*,SYSTEM*,int);
double fdTotOrbEnergy(BODY*, CONTROL*, SYSTEM*);
double fdKinEnergy(BODY*,CONTROL*,SYSTEM*,int);
double fdPotEnergy(BODY*,CONTROL*,SYSTEM*,int);
double fdTotEnergy(BODY*,CONTROL*,SYSTEM*);

int bPrimary(BODY*,int);


void CalcHK(BODY*,int);
void CalcPQ(BODY*,int);

/* Multi-body derivative equations */
double fdSemiDtEqSt(BODY*,SYSTEM*,int*);
double fdJStarDt(BODY*,int);
double fdJBrakingStarDt(BODY*,int);
double fdRadiusStarDt(BODY*,int);
double fdSemiTidalLockBinEqSt(BODY*,int,int);
double fndUpdateSpiNBodyCoords(BODY*,EVOLVE*);
