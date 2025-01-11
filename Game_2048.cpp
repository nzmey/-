
// ���� 2048.

// ��� ���� ������� ������������ �������� ����������.
// "8" - �����.
// "2" - ����.
// "4" - �����.
// "6" - ������.
// ����� ����� ����� - ������� ������ "Enter".
// ��� ����� ������-���� ����� ����� - ���������
// ����������� ������ ���������� �����.
// �� ��������� - ��� � � ������� ����.

#include<iostream>
#include<Windows.h>
#include<ctime>

using namespace std;

// ������ ������� �����������.
const int Size_16 =16;

// ������ �����������.
int Arr[Size_16];

// ������, �������� ���������� �������� ������� "Arr".
int Arr_CTRL[Size_16];


///////////////////////////////////////////////////////////////////////////////


// ������� �������������.
void Func_Arr_get(int k=0);

// ������� �������.
void Func_Arr_Show();

// ������� ���������� ������.
void Func_Cell_Tag();

// ������� �����.
void Func_Sum(int &a, int &b, int &c, int &d);

// �������� ����������� ���� � ������.
void Func_Ctrl_Str(int a, int b, int c, int d);

// ����� �������� ����������� ����.
void Func_Ctrl_Common();

// ������� ���� ������.
void Func_Path();

// ������� �����������.
void Func_Diff();

// ������� �ר���� ����� � ������� "Arr".
void Func_Arr_Sum();

// ������� ����������� �������� ������� "Arr" �� ����� 2948.
void Func_2048();


///////////////////////////////////////////////////////////////////////////


// �ר���� ������.
int CNT_SUM;

// �ר���� �����.
int CNT_PAS;

// ����������� �������.
bool STOP, STOP_WHILE;


//////////////////////////////////////////////////////////////////////////


// ��������. ����������� ����� "�����" � "�������".
int v_2=0, v_4=0;

int main(){

	cout<<"\n\n\n\tBEGIN!!!\n\n\n";

	// ����� ���������� �����.
	int a=0;
	a = (int)time(nullptr);
	srand(a);
//	cout<<"\n\n\ttime(nullptr) = "<<a;

	CNT_PAS =0;
	CNT_SUM =0;
	STOP_WHILE =1;
	STOP =1;

	Func_Arr_get(); // ������������� ��������.
	Func_Cell_Tag(); // ��������� ������ ������.

	while(STOP)
	{
		cout<<"\n\n\tCNT_PAS : "<<CNT_PAS;

		Func_Cell_Tag(); // ��������� �����.
		if(STOP==0)break;

		Func_Arr_Sum(); // ������� ����� �����, ������������ � ������� �������.		

		cout<<"\n\n\tCNT_SUM = "<<CNT_SUM<<"\n\n";
		
		Func_Arr_Show(); // ����� �� �����.

		Func_2048(); // ���� �� 2048?
		if(STOP==0)break;

				
		Func_Ctrl_Common(); // �������� ����������� ���������� ���� ������.
		if(STOP==0)
		{
//			cout<<"\n\n\tSTOP = "<<STOP;
			cout<<"\n\n\tGAME OVER!!!\n\n";
			break;
		}

		STOP_WHILE =1;
		while(STOP_WHILE)
		{
			Func_Path(); // ��� ������.

			Func_Diff(); // ��������� �������� ������� � ��� ���������� ����������.
			if(STOP_WHILE==0) break;
		}
		if(STOP==0) break;

		CNT_PAS++; // ������� ����� ������.

//		if(CNT_PAS		>	3	) break;
	}

	cout<<"\n\n\n\n\n\tEND!!!\n\n\t";

return 0;
}

////////////////////////////////////////////////////////////////////////

// ������� �������������.
void Func_Arr_get(int k)
{
	int i=0;
//	k=i;
//	k=(i+1);
	for(i=0;i<Size_16;i++)
	{
		Arr[i] =k;
		Arr_CTRL[i] =0;
	}
}

///////////////////////////////////////////////////////////////////////

// ������� �������.
void Func_Arr_Show()
{
//	cout<<"\n\n";
	int i =0;
	for(i=0;i<Size_16;i++)
	{
		(i%4)?(	cout<<"\t\t"<<Arr[i]):(cout<<"\n\n\n\n\t\t"<<Arr[i]);
	}
}

//////////////////////////////////////////////////////////////////////////

// ������� ���������� ������.
void Func_Cell_Tag()
{
	int Val =0, INDEX =(-1), jump=0, bit =0;

	int temp_Rand = rand();
//	cout<<"\n\n\ttemp_Rand = "<<temp_Rand;

	// ����� "�����" �� "�������" �������.
	jump = temp_Rand % 16;
//	cout<<"\tjump = "<<jump;

	// ������� �����.
	bit = (temp_Rand & 7);
	(bit)?(Val=2):(Val=4);
//	cout<<"\tbit = "<<bit;
//	cout<<"\tVal = "<<Val<<"\n";

	// ������� �����������.
	(bit)?(v_2++):(v_4++);

	// ���������� ������ ������.
	int i=0, j=(-1), arr_Index[Size_16], a=0, turn=0;

	// "���������" ������� ������� �����.
	a=0;
	for(a=0;a<Size_16;a++)
	{	arr_Index[a]=(-1);	}

	// ���������� ������� ������� �����.
	a=0;
	for(i=0;i<Size_16;i++)
	{
		if(Arr[i]==0)
		{
			arr_Index[a]=i;
//			cout<<"\n\tarr_Index["<<a<<"]= "<<arr_Index[a];
			a++;
		}
	}

	// ���������� ���������� ��������� ������� ������� �����.
	for(;((a < Size_16)&&(turn < Size_16));a++, turn++)
	{
		arr_Index[a]= arr_Index[turn];
//		cout<<"\n\tarr_Index["<<a<<"]= "<<arr_Index[a];
	}

	// ����� ������.
	INDEX = arr_Index[jump];
	

	// �������� ������������ ������.
	if(((-1) < INDEX)&&(INDEX < Size_16))
		{
			Arr[INDEX] =Val;
//			cout<<"\n\n\tArr["<<INDEX<<"] = "<<Arr[INDEX];
		}
	else
		{
			STOP =0; // ���������� ���������� ����������� ������.
			cout<<"\n\n\tPOLUNDRA!!!!!!!!!!";
			cout<<"\n\n\tINDEX = "<<INDEX;
		}
//	cout<<"\n\n\tv_2 = "<<v_2<<"\tv_4 = "<<v_4;

	// "���������" ������� ������� �����.
	a=0;
	for(a=0;a<Size_16;a++)
	{	arr_Index[a]=(-1);	}

	// ��������� ����������.
	Val=0; INDEX=(-1); temp_Rand=0; jump=0; bit=0; a=0; turn=0;
}

//////////////////////////////////////////////////////////////////////////////////////////

// ������� �����.
void Func_Sum(int &a, int &b, int &c, int &d)
{
	int ar[4], i=0, j=0;
	ar[0] =a; ar[1] =b; ar[2] =c; ar[3] =d;
//	cout<<"\n\n\tAr = "<<a<<"  "<<b<<"  "<<c<<"  "<<d<<"\n";

	// �����.
	i=0; j=0;
	for(j=0;j<2;j++)
	{
		for(i=0;i<3;i++)
		{
			if(ar[i]==0)
			{
				ar[i] = ar[i+1];
				ar[i+1] =0;
			}
		}
	}
//	a =ar[0]; b =ar[1]; c=ar[2]; d =ar[3];
//	cout<<"\n\n\tAr = "<<a<<"  "<<b<<"  "<<c<<"  "<<d<<"\n";

	// ��������.
	i=0;
	for(i=0;i<3;i++)
	{
		if((ar[i])&&(ar[i]==ar[i+1]))
		{
			(ar[i]) <<= 1;
			ar[i+1]   = 0;
		}
	}
//	a =ar[0]; b =ar[1]; c=ar[2]; d =ar[3];
//	cout<<"\n\n\tAr = "<<a<<"  "<<b<<"  "<<c<<"  "<<d<<"\n";


	// �����.
	i=0; j=0;
	for(j=0;j<2;j++)
	{
		for(i=0;i<3;i++)
		{
			if(ar[i]==0)
			{
				ar[i] = ar[i+1];
				ar[i+1] =0;
			}
		}
	}

	a=ar[0]; b=ar[1]; c=ar[2]; d=ar[3];
//	cout<<"\n\n\tAr = "<<a<<"  "<<b<<"  "<<c<<"  "<<d<<"\n";
//	CNT_SUM +=ar[0] +=ar[1] +=ar[2] +=ar[3];
	ar[0] = ar[1] = ar[2] = ar[3] =0;
}

////////////////////////////////////////////////////////////////////////////////////

// ������� �������� ����������� ���� � ������.
void Func_Ctrl_Str(int a, int b, int c, int d)
{
	int arr[4], i=0;
	arr[0] =a; arr[1] =b; arr[2] =c; arr[3] =d;
//	cout<<"\n\n\tAr = "<<a<<"  "<<b<<"  "<<c<<"  "<<d<<"\n";

	i=0;
	for(i=0;i<3;i++)
	{
		if((arr[i])==(arr[i+1]))
		{
			STOP=1;
			break;
		}
	}
//	cout<<"\n\n\tFunc_Ctrl_Str : STOP = "<<STOP;
}

/////////////////////////////////////////////////////////////////////////////////////////////

// ������� ����� �������� ����������� ����.
void Func_Ctrl_Common()
{
	STOP =0; //

	int i=0;
	for(i=0;i<Size_16;i++)
	{
		if(Arr[i]==0)
		{
			STOP =1;
			break;
		}
	}
//	cout<<"\n\n\tSTOP = "<<STOP;

	if(STOP==0)
	{
		Func_Ctrl_Str(Arr[0], Arr[1], Arr[2], Arr[3]);
		Func_Ctrl_Str(Arr[4], Arr[5], Arr[6], Arr[7]);
		Func_Ctrl_Str(Arr[8], Arr[9], Arr[10], Arr[11]);
		Func_Ctrl_Str(Arr[12], Arr[13], Arr[14], Arr[15]);

		Func_Ctrl_Str(Arr[0], Arr[4], Arr[8], Arr[12]);
		Func_Ctrl_Str(Arr[1], Arr[5], Arr[9], Arr[13]);
		Func_Ctrl_Str(Arr[2], Arr[6], Arr[10], Arr[14]);
		Func_Ctrl_Str(Arr[3], Arr[7], Arr[11], Arr[15]);

//		cout<<"\n\n\tFunc_Ctrl_Common: TEST IS GOON!!!";
	}
}

///////////////////////////////////////////////////////////////////////////////////////////////

// ������� ���� ������.
void Func_Path()
{
	int ch =0, i=0;

	STOP_WHILE =0; //

	// ������ ��������� �������� ������� "Arr" � ����������� ������.
	for(i=0;i<Size_16;i++)
	{
		Arr_CTRL[i]=Arr[i];
	}

	loop:
	cout<<"\n\n\tEnter Integer: ___\b\b";
	cin>>ch;

	switch(ch)
	{
				case 4:
		Func_Sum(Arr[0], Arr[1], Arr[2], Arr[3]);
		Func_Sum(Arr[4], Arr[5], Arr[6], Arr[7]);
		Func_Sum(Arr[8], Arr[9], Arr[10], Arr[11]);
		Func_Sum(Arr[12], Arr[13], Arr[14], Arr[15]);
			break;
				case 6:
		Func_Sum(Arr[3], Arr[2], Arr[1], Arr[0]);
		Func_Sum(Arr[7], Arr[6], Arr[5], Arr[4]);
		Func_Sum(Arr[11], Arr[10], Arr[9], Arr[8]);
		Func_Sum(Arr[15], Arr[14], Arr[13], Arr[12]);
		break;
				case 8:
		Func_Sum(Arr[0], Arr[4], Arr[8], Arr[12]);
		Func_Sum(Arr[1], Arr[5], Arr[9], Arr[13]);
		Func_Sum(Arr[2], Arr[6], Arr[10], Arr[14]);
		Func_Sum(Arr[3], Arr[7], Arr[11], Arr[15]);
		break;
				case 2:
		Func_Sum(Arr[12], Arr[8], Arr[4], Arr[0]);
		Func_Sum(Arr[13], Arr[9], Arr[5], Arr[1]);
		Func_Sum(Arr[14], Arr[10], Arr[6], Arr[2]);
		Func_Sum(Arr[15], Arr[11], Arr[7], Arr[3]);
		break;
				default:
		goto loop;
	}
}

////////////////////////////////////////////////////////////////////////////////////////////////

// ������� ����������� �������� ������� � ����������� ��������.
void Func_Diff()
{
	int i=0, stop =1;
	for(i=0;i<Size_16;i++)
	{
		if((Arr[i]) != (Arr_CTRL[i]))
		{
			stop =0;
			break;
		}
	}
	if(stop)
	{
//		cout<<"\n\n\tFunc_Diff() : Litle stop = "<<stop;
		cout<<"\n\n\tEnter NEW PAS!!!\n\n";

		STOP_WHILE =1;
	}
}

///////////////////////////////////////////////////////////////////////////////////////////////

// ������� �ר���� ����� � ������� ������� "Arr".
void Func_Arr_Sum()
{
	CNT_SUM=0;
	int i=0;
	for(i=0;i<Size_16;i++)
		CNT_SUM +=Arr[i];
}

///////////////////////////////////////////////////////////////////////////////////////////////

// ������� ����������� �������� ������� "Arr" �� ����� 2048.
void Func_2048()
{
	int i=0;
	for(i=0;i<Size_16;i++)
	{
		if(Arr[i] > 2047)
		{
			cout<<"\n\n\tYES!!! 2048 IS REACH!!!";
			STOP =0;
		}
	}
}
