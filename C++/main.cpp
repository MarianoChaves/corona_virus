#include "includes.hpp"

vector <double> data;
vector <int> days;
int N;

/* ############################################################## */
/* ############################################################## */


double cases_per_day(double *x,int i)
{
	return x[0] + pow(2,i/x[1]);
}


double Chi2_COVID19(double *x)
{


	double chi2 = 0;


/////////////////////////////////////

	for(int i = 0; i< N; i++)
	{
		double theo =cases_per_day(x,days[i]);
		
		chi2 += pow(theo-data[i],2)/theo;		
	};

	return chi2;

};


double MinimizerMC(double (*f) (double*), double *param, double *guess, double *inf_bounds, double *sup_bounds, int num_param, double *param_step, int steps)
{



	double min=20000000;
	double localmin = 10000000;
	double init[num_param];	
	double param_min[num_param];
	double param_localmin[num_param];
	for(int i=0; i< num_param; i++){init[i]=guess[i];param_min[i]=guess[i];};
	srand(time(NULL));



	for(int i=0; i<steps; i++)
	{
		double test;


		
		for(int j=0; j<num_param; j++)
		{	
			if(inf_bounds[j]!=sup_bounds[j]){	
				do{				
						param[j] = init[j] + param_step[j]*(1.-2.*float((rand() % 2)));
				}while( (param[j] < inf_bounds[j]) or (param[j] > sup_bounds[j]) );
			};
		};
		test = (*f)(param);


		if(test<localmin)
		{
			for(int j=0; j<num_param; j++){init[j] = param[j];param_localmin[j] = param[j];};
			localmin=test;
			if(localmin<min){
				min=localmin;
					for(int j=0; j<num_param; j++)
					{
						param_min[j] = param_localmin[j];
					};
			};		
		}
		else
		{
			int trial = (rand() % 100);
			if(trial<30)
			{
				for(int j=0; j<num_param; j++){init[j] = param[j];};
				localmin=test;
			};
		};



	};

	for(int j=0; j<num_param; j++){param[j] = param_min[j];};

	return min;

}




int main(int argc, char *argv[])
{ 	


/***************************************************************************
 *                        I N I T I A L I Z A T I O N                      *
 ***************************************************************************/
/////////////////// Reading File

FILE *datafile;
datafile = fopen("data/dados_novos.dat","r");

fscanf(datafile,"number of data: %d\n\n",&N);

float aux;
int count, day, month;

for(int i = 0; i< N; i++)
{
	fscanf(datafile,"%d\t%f\n", &count, &aux);
	data.push_back(double(aux));
	days.push_back(double(count));



};
fclose(datafile);


ofstream outfile1("results.dat");





/***************************************************************************
 *                             S I M U L A T I O N                         *
 ***************************************************************************/ 

//////////////////////////////////////////////////////////////////////////////
/////////////////////////   Parameters  Running   ////////////////////////////













/////////////////////////////////////////////////////////////////////////////
////////////////////    Montecarlo Inicialization   /////////////////////////



double guess[2] = {0.0, 2.5};
double param_min[2] = {-0.5, 2.};
double param_max[2] = {2., 3.};
double param[2] = {0., 2.};

double param_step[2]={0.01};

int steps = 10000;


double chi2min=0.0;


//chi2min = Chi2_COVID19(guess);

chi2min = MinimizerMC(Chi2_COVID19, param, guess, param_min, param_max, 2, param_step, steps);

printf("param_1: %f, param_2: %f, Chi²: %f\n",param[0], param[1], chi2min);

int M =1000;

double d[2] = {(param_max[0]-param_min[0])/M,(param_max[1]-param_min[1])/M};


vector <double> param_90_1;
vector <double> param_90_2;

double Dchi2=1000000;

double param_test[2];
double cases_max[60];
double cases_min[60];

for(int k=0; k<60; k++)
{
	cases_max[k]=-1000000;
	cases_min[k]=1000000;
for(int i=0; i<M; i++)
{
for(int j=0; j<M; j++)
{		
	 param_test[0] = param_min[0]+d[0]*i;
	 param_test[1] = param_min[1]+d[1]*j;

	Dchi2 = Chi2_COVID19(param_test);

	if(abs(Dchi2-chi2min-6.635)<0.01){
		double cases_test = cases_per_day(param_test,k);
		if(cases_min[k]>cases_test){cases_min[k]=cases_test;};
		if(cases_max[k]<cases_test){cases_max[k]=cases_test;};		
	};
	


};
};
};


/////////////////////////////////////////////////////////////////////////////
/////////////////////         File Wiriting       ///////////////////////////

for(int i = 0; i<60; i++){	outfile1<<i<<"\t"<<int(cases_per_day(param,i))<<"\t"<<int(cases_min[i])<<"\t"<<int(cases_max[i])<<endl;};

outfile1.close();

}
// main program ends!

/* ############################################################## */
/* ############################################################## */


