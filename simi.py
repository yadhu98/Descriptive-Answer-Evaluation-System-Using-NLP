from nltk import sent_tokenize,word_tokenize,PorterStemmer
from nltk.corpus import wordnet,stopwords
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
import math,re
from collections import Counter
import numpy as np




input_text=open("model.txt","r")
input_text1=open("ans1.txt","r")
input_text2=open("ans2.txt","r")
input_text3=open("ans3.txt","r")
input_text4=open("ans4.txt","r")
input_text5=open("ans5.txt","r")
input_text6=open("ans6.txt","r")
input_text7=open("ans7.txt","r")
input_text8=open("ans8.txt","r")
input_text9=open("ans9.txt","r")
input_text10=open("ans10.txt","r")
text=input_text.read()
text1=input_text1.read()
text2=input_text2.read()
text3=input_text3.read()
text4=input_text4.read()
text5=input_text5.read()
text6=input_text6.read()
text7=input_text7.read()
text8=input_text8.read()
text9=input_text9.read()
text10=input_text10.read()
input_text.close()
input_text1.close()
input_text2.close()
input_text3.close()
input_text4.close()
input_text5.close()
input_text6.close()
input_text7.close()
input_text8.close()
input_text9.close()
input_text10.close()
sentences=sent_tokenize(text)
sentences1=sent_tokenize(text1)
sentences2=sent_tokenize(text2)
sentences3=sent_tokenize(text3)
sentences4=sent_tokenize(text4)
sentences5=sent_tokenize(text5)
sentences6=sent_tokenize(text6)
sentences7=sent_tokenize(text7)
sentences8=sent_tokenize(text8)
sentences9=sent_tokenize(text9)
sentences10=sent_tokenize(text10)
N=len(sentences)
N1=len(sentences1)
N2=len(sentences2)
N3=len(sentences3)
N4=len(sentences4)
N5=len(sentences5)
N6=len(sentences6)
N7=len(sentences7)
N8=len(sentences8)
N9=len(sentences9)
N10=len(sentences10)



ps=PorterStemmer()
lemmatizer=WordNetLemmatizer()
stop_words=stopwords.words('english')
special=['.',',','\'','"','-','/','*','+','=','!','@','$','%','^','&','``','\'\'','We','The','This']






def normalise(word):
    word = word.lower()
    word = ps.stem(word)
    return word


def get_cosine(vec1, vec2):
     intersection = set(vec1) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return numerator / denominator


def text_to_vector(text):
     words = word_tokenize(text)
     vec=[]
     for word in words:
         if(word not in stop_words):
             if(word not in special):
                 w=normalise(word);
                 vec.append(w);
     #print Counter(vec)
     return Counter(vec)



def docu_to_vector(sent):
     vec=[]
     for text in sent:
         words = word_tokenize(text)
         for word in words:
             if(word not in stop_words):
                 if(word not in special):
                     w=normalise(word);
                     vec.append(w);
     #print Counter(vec)
     return Counter(vec)




def f_s_to_s(sent):
    cosine_mat=np.zeros(N+1)
   
    row=0
    for text in sentences:
        maxi=0
        vector1 = text_to_vector(text)
        for text1 in sent:
            vector2 = text_to_vector(text1)
            cosine = get_cosine(vector1, vector2)

        for text2 in sent:
            vector3 = text_to_vector(text2)
            cosine = get_cosine(vector1, vector3)

        for text3 in sent:
            vector4 = text_to_vector(text3)
            cosine = get_cosine(vector1, vector4)


        for text4 in sent:
            vector5 = text_to_vector(text4)
            cosine = get_cosine(vector1, vector5)
       
        for text5 in sent:
            vector6 = text_to_vector(text5)
            cosine = get_cosine(vector1, vector6)

        for text6 in sent:
            vector7 = text_to_vector(text6)
            cosine = get_cosine(vector1, vector7)

        for text7 in sent:
            vector8 = text_to_vector(text7)
            cosine = get_cosine(vector1, vector8)


        for text8 in sent:
            vector9 = text_to_vector(text4)
            cosine = get_cosine(vector1, vector9)

        for text9 in sent:
            vector10 = text_to_vector(text9)
            cosine = get_cosine(vector1, vector10)
            
            if(maxi<cosine):
                maxi=cosine
               
        cosine_mat[row]=maxi
             
        row+=1
        
    return cosine_mat   
    
def main():

    sent = sentences1 + sentences2 + sentences3 + sentences4 + sentences5
    max_mark= 3
    mat = f_s_to_s(sentences1)
    mat1 = f_s_to_s(sentences2)
    mat2 = f_s_to_s(sentences3)
    mat3 = f_s_to_s(sentences4)
    mat4 = f_s_to_s(sentences5)
    mat5 = f_s_to_s(sentences6)
    mat6 = f_s_to_s(sentences7)
    mat7 = f_s_to_s(sentences8)
    mat8 = f_s_to_s(sentences9)
    mat9 = f_s_to_s(sentences10)
    
    point1= sum(mat)
    point2=sum(mat1)
    point3=sum(mat2)
    point4=sum(mat3)
    point5=sum(mat4)
    point6=sum(mat5)
    point7=sum(mat6)
    point8=sum(mat7)
    point9=sum(mat8)
    point10=sum(mat9)   
    score1= point1 * max_mark/(N)
    score2= point2 * max_mark/(N)
    score3= point3 * max_mark/(N)
    score4= point4 * max_mark/(N)
    score5= point5 * max_mark/(N)
    score6= point6 * max_mark/(N)
    score7= point7 * max_mark/(N)
    score8= point8 * max_mark/(N)
    score9= point9 * max_mark/(N)
    score10= point10 * max_mark/(N) 
   
    print score1
    print score2
    print score3
    print score4
    print score5
    print score6
    print score7
    print score8
    print score9
    print score10   
if __name__ == '__main__':
    main()
   
   

  
