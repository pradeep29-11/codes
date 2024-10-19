{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b6b080ae-f6a8-4b01-a339-19490b41aecc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20\n"
     ]
    }
   ],
   "source": [
    "a=20\n",
    "print(a)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fca05c44-4f5d-4267-b7d0-c80e3b106e4c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*****\n",
      "*****\n",
      "*****\n",
      "*****\n",
      "*****\n"
     ]
    }
   ],
   "source": [
    "#square \n",
    "for i in range(0,5):\n",
    "    for i in range(0,5):\n",
    "        print(\"*\",end=\"\")\n",
    "    print()\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "bdc87b15-fffa-4f00-86f4-3ef4581c395f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "# \n",
      "# # \n",
      "# # # \n",
      "# # # # \n",
      "# # # # # \n"
     ]
    }
   ],
   "source": [
    "#right angle\n",
    "for i in range(0,5):\n",
    "    for i in range(0,i+1):\n",
    "        print(\"#\",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "dae5e392-6319-4525-86e1-8dffc89ef078",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*****\n",
      " ****\n",
      "  ***\n",
      "   **\n",
      "    *\n"
     ]
    }
   ],
   "source": [
    "#left triangle\n",
    "for i in range(4,-1,-1):\n",
    "    print(\" \"*(4-i),end=\"\")\n",
    "    for j in range(0,i+1):\n",
    "        print(\"*\",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ebfc475d-1c6b-4b32-b9f8-9b557d983822",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "*****\n",
      " ****\n",
      "  ***\n",
      "   **\n",
      "    *\n"
     ]
    }
   ],
   "source": [
    "for i in range(4,-1,-1):\n",
    "    print(\" \"*(4-i),end=\"\")\n",
    "    \n",
    "    for j in range(0,i+1):\n",
    "        print(\"*\",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1d736fdf-4580-4177-bf6d-3726b1a7d77a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "# \n",
      "# # \n",
      "# # # \n",
      "# # # # \n",
      "# # # # # \n"
     ]
    }
   ],
   "source": [
    "for i in range(0,5):\n",
    "    for i in range(0,i+1):\n",
    "        print(\"#\",end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8224addb-1ac6-4f72-a0b1-a95a0c6a82a7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0001 0002 0003 0004 0005 0006 0007 0008 0009 0010 \n",
      "0002 0004 0006 0008 0010 0012 0014 0016 0018 0020 \n",
      "0003 0006 0009 0012 0015 0018 0021 0024 0027 0030 \n",
      "0004 0008 0012 0016 0020 0024 0028 0032 0036 0040 \n",
      "0005 0010 0015 0020 0025 0030 0035 0040 0045 0050 \n",
      "0006 0012 0018 0024 0030 0036 0042 0048 0054 0060 \n",
      "0007 0014 0021 0028 0035 0042 0049 0056 0063 0070 \n",
      "0008 0016 0024 0032 0040 0048 0056 0064 0072 0080 \n",
      "0009 0018 0027 0036 0045 0054 0063 0072 0081 0090 \n",
      "0010 0020 0030 0040 0050 0060 0070 0080 0090 0100 \n"
     ]
    }
   ],
   "source": [
    "#table\n",
    "for i in range(1,11):\n",
    "    for j in range(1,11):\n",
    "        print(\"%04d \"%(i*j),end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "66161d24-bb49-4c9b-8285-0362afae0a1b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   1   2   3   4   5   6   7   8   9  10\n",
      "   2   4   6   8  10  12  14  16  18  20\n",
      "   3   6   9  12  15  18  21  24  27  30\n",
      "   4   8  12  16  20  24  28  32  36  40\n",
      "   5  10  15  20  25  30  35  40  45  50\n",
      "   6  12  18  24  30  36  42  48  54  60\n",
      "   7  14  21  28  35  42  49  56  63  70\n",
      "   8  16  24  32  40  48  56  64  72  80\n",
      "   9  18  27  36  45  54  63  72  81  90\n",
      "  10  20  30  40  50  60  70  80  90 100\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,11):\n",
    "    for j in range(1,11):\n",
    "        print(\"%4d\"%(i*j),end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "7e5d3de5-13c1-4979-a314-e88123dc68ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "AAAAA\n",
      "BBBBB\n",
      "CCCCC\n",
      "DDDDD\n"
     ]
    }
   ],
   "source": [
    "for i in range(ord(\"A\"),ord(\"E\")):\n",
    "    for j in range(0,5):\n",
    "        print(chr(i),end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "raw",
   "id": "8842595b-e5ad-4a38-b4dd-7dc28299f003",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "345b7821-6310-480f-9e7a-77a6bfecf4ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\n",
      "bb\n",
      "ccc\n",
      "dddd\n",
      "eeeee\n",
      "ffffff\n"
     ]
    }
   ],
   "source": [
    "for i in range(ord(\"a\"),ord(\"g\")):\n",
    "    for j in range(ord(\"a\"),i+1):\n",
    "        print(chr(i),end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "c51d5727-375a-4681-9495-ff1374490ce4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ABCD\n",
      "ABCD\n",
      "ABCD\n",
      "ABCD\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,5):\n",
    "    for j in range(1,5):\n",
    "        print(chr(64+j),end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "d0cbca13-a467-46b1-ae8b-7e95406cfc17",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "######\n",
      "#####\n",
      " ####\n",
      "  ###\n",
      "   ##\n",
      "    #\n"
     ]
    }
   ],
   "source": [
    "for i in range(5,-1,-1):\n",
    "    print(\" \"*(4-i),end=\"\")\n",
    "    for j in range(0,i+1):\n",
    "        print(\"#\",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "ed3a8c8c-f116-43b7-9b79-ac18b22dade7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    #\n",
      "   ##\n",
      "  ###\n",
      " ####\n",
      "#####\n"
     ]
    }
   ],
   "source": [
    "for i in range(0,5):\n",
    "    print(\" \"*(4-i),end=\"\")\n",
    "    for j in range(0,i+1):\n",
    "        print(\"#\",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "bcab33d8-1658-4d93-8610-1c071e1e9f50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n"
     ]
    }
   ],
   "source": [
    "a=65\n",
    "print(chr(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "f48321df-0747-423f-8c50-e42040870e9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "65\n"
     ]
    }
   ],
   "source": [
    "a=\"A\"\n",
    "print(ord(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "3ed381b2-aa7d-4925-b3bb-eea04828774f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    * \n",
      "   * * \n",
      "  * * * \n",
      " * * * * \n",
      "* * * * * \n"
     ]
    }
   ],
   "source": [
    "for i in range(0,5):\n",
    "    print(\" \"*(4-i),end=\"\")\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "raw",
   "id": "c67ed710-cca7-4089-a132-b7ff817f595c",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "57d1657b-cde9-44c6-a6f2-ecf9c773d9d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "* * * * * \n",
      " * * * * \n",
      "  * * * \n",
      "   * * \n",
      "    * \n"
     ]
    }
   ],
   "source": [
    "for i in range(4,-1,-1):\n",
    "    print(\" \"*(4-i),end=\"\")\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "99e91fd3-e95f-4a64-97d2-af28898d18f7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    * \n",
      "   * * \n",
      "  * * * \n",
      " * * * * \n",
      "* * * * * \n",
      " * * * * \n",
      "  * * * \n",
      "   * * \n",
      "    * \n"
     ]
    }
   ],
   "source": [
    "for i in range(0,5):\n",
    "    print(\" \"*(4-i),end=\"\")\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()\n",
    "\n",
    "for i in range(3,-1,-1):\n",
    "    print(\" \"*(4-i),end=\"\")\n",
    "    for j in range(0,i+1):\n",
    "        print(\"* \",end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "29385264-3426-404e-923a-89be8d11c781",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "80\n"
     ]
    }
   ],
   "source": [
    "print(ord(\"P\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "30ce469f-e58c-4cc6-b282-c974ccd965d9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PQRST\n",
      "PQRST\n",
      "PQRST\n",
      "PQRST\n",
      "PQRST\n"
     ]
    }
   ],
   "source": [
    "for i in range(0,5):\n",
    "    for j in range(0,5):\n",
    "        print(chr(j+80),end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "85c57e32-3895-4c15-ac07-c41ea3f4b579",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PPPPP\n",
      "QQQQQ\n",
      "RRRRR\n",
      "SSSSS\n",
      "TTTTT\n"
     ]
    }
   ],
   "source": [
    "for i in range(0,5):\n",
    "    for j in range(0,5):\n",
    "        print(chr(80+i),end=\"\")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "b6dcb53a-1157-4fd7-acf2-9bd825f1bb7d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data=10\n",
      "Data=11\n",
      "Data=13\n"
     ]
    }
   ],
   "source": [
    "a=10\n",
    "b=11\n",
    "c=13\n",
    "print(\"Data=%2d\"%a)\n",
    "print(\"Data=%d\"%b)\n",
    "print(\"Data=%d\"%c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "68dcb939-cf5e-4651-a38f-27718819bd18",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data=111\n",
      "Data=022\n",
      "Data=003\n"
     ]
    }
   ],
   "source": [
    "a=111\n",
    "b=22\n",
    "c=3\n",
    "print(\"Data=%03d\"%a)\n",
    "print(\"Data=%03d\"%b)\n",
    "print(\"Data=%03d\"%c)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "ffab1970-0b69-4d5d-88b4-2211ff3c2905",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "21703fdb-5741-40a8-9905-d922c66bb258",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$$$$\n"
     ]
    }
   ],
   "source": [
    "print(\"$\"*4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d28fd4f4-4f0a-460d-9a50-0827088b8204",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
