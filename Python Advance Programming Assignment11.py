#!/usr/bin/env python
# coding: utf-8

# 1. Create a function that takes a list and returns a new list containing only
# prime numbers.
# Examples
# filter_primes([7, 9, 3, 9, 10, 11, 27]) ➞ [7, 3, 11]
# filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) ➞ [10007, 1009]
# filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093,
# 1097]) ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


def filter_primes(in_list):
    out_list = []
    for ele in in_list:
        if ele in [2,3]:
            out_list.append(ele)
        elif ((ele+1)%6 == 0) or ((ele-1)%6 == 0) and ele != 1:
            out_list.append(ele)
    temp = out_list.copy()
    for ele in temp:
        for num in range(2,ele):
            if ele%num == 0:
                out_list.remove(ele)
                break        
    print(f'filter_primes({in_list}) ➞ {out_list}')
    
filter_primes([7, 9, 3, 9, 10, 11, 27])
filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70])
filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097])


# 2. Once a water balloon pops, is soaks the area around it. The ground gets
# drier the further away you travel from the balloon.
# The effect of a water balloon popping can be modeled using a list. Create a
# function that takes a list which takes the pre-pop state and returns the state
# after the balloon is popped. The pre-pop state will contain at most a single
# balloon, whose size is represented by the only non-zero element.
# Examples
# pop([0, 0, 0, 0, 4, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4, 3, 2, 1, 0]
# pop([0, 0, 0, 3, 0, 0, 0]) ➞ [0, 1, 2, 3, 2, 1, 0]
# pop([0, 0, 2, 0, 0]) ➞ [0, 1, 2, 1, 0]
# pop([0]) ➞ [0]
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


def pop(in_list):
    pop_number = sorted(in_list,reverse=True)[0]
    output = []
    if pop_number == 0:
        output.append(0)
    else:
        output.extend([x for x in range((len(in_list)-1)//2)])
        output.append(pop_number)
        output.extend([((len(in_list)-2)//2)-x for x in range((len(in_list)-1)//2)])
    print(f'pop({in_list}) ➞ {output}')
    
pop([0, 0, 0, 0, 4, 0, 0, 0, 0])
pop([0, 0, 0, 3, 0, 0, 0])
pop([0, 0, 2, 0, 0])
pop([0])


# 3. &quot;Loves me, loves me not&quot; is a traditional game in which a person plucks off
# all the petals of a flower one by one, saying the phrase &quot;Loves me&quot; and
# &quot;Loves me not&quot; when determining whether the one that they love, loves them
# back.
# Given a number of petals, return a string which repeats the phrases &quot;Loves
# me&quot; and &quot;Loves me not&quot; for every alternating petal, and return the last phrase
# in all caps. Remember to put a comma and space between phrases.
# Examples
# loves_me(3) ➞ &quot;Loves me, Loves me not, LOVES ME&quot;
# loves_me(6) ➞ &quot;Loves me, Loves me not, Loves me, Loves me not, Loves
# me, LOVES ME NOT&quot;
# 
# loves_me(1) ➞ &quot;LOVES ME&quot;
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def loves_me(in_num):
    out_string = []
    for ele in range(in_num):
        if ele%2 ==0:
            out_string.append('Loves me')
        else:
            out_string.append('Loves me not')
    out_string[-1] = out_string[-1].upper()
    print(f'loves_me({in_num}) ➞ {", ".join(out_string)}')
    
loves_me(3)
loves_me(6)
loves_me(1)


# 4. Write a function that sorts each string in a list by the letter in alphabetic
# ascending order (a-z).
# Examples
# sort_by_letter([&quot;932c&quot;, &quot;832u32&quot;, &quot;2344b&quot;])
# ➞ [&quot;2344b&quot;, &quot;932c&quot;, &quot;832u32&quot;]
# sort_by_letter([&quot;99a&quot;, &quot;78b&quot;, &quot;c2345&quot;, &quot;11d&quot;])
# ➞ [&quot;99a&quot;, &quot;78b&quot;, &quot;c2345&quot;, &quot;11d&quot;]
# sort_by_letter([&quot;572z&quot;, &quot;5y5&quot;, &quot;304q2&quot;])
# ➞ [&quot;304q2&quot;, &quot;5y5&quot;, &quot;572z&quot;]
# sort_by_letter([])
# ➞ []
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def sort_by_letter(in_list):
    temp_list = []
    output = []
    for ele in in_list:
        for char in ele:
            if char.isalpha():
                temp_list.append(char)
    temp_list.sort()
    for char in temp_list:
        for ele in in_list:
            if char in ele:
                output.append(ele)
    
    print(f'sort_by_letter({in_list}) ➞ {output}')
                
sort_by_letter(["932c", "832u32", "2344b"])
sort_by_letter(["99a", "78b", "c2345", "11d"])
sort_by_letter(["572z", "5y5", "304q2"])
sort_by_letter([])


# 5. There are three cups on a table, at positions A, B, and C. At the start, there
# is a ball hidden under the cup at position B.
# 
# However, I perform several swaps on the cups, which is notated as two
# letters. For example, if I swap the cups at positions A and B, I could notate
# this as AB or BA.
# Create a function that returns the letter position that the ball is at, once I finish
# swapping the cups. The swaps will be given to you as a list.
# 
# Example
# cup_swapping([&quot;AB&quot;, &quot;CA&quot;, &quot;AB&quot;]) ➞ &quot;C&quot;
# # Ball begins at position B.
# # Cups A and B swap, so the ball is at position A.
# # Cups C and A swap, so the ball is at position C.
# # Cups A and B swap, but the ball is at position C, so it doesn&#39;t move.
# 
# 
# 
# 
# 
# 
# Ans:-

# In[6]:


def cup_swapping(swap_list,intitial_ball_pos):
    ball_position = intitial_ball_pos
    for ele in swap_list:
        if ball_position in ele:
            ball_position = ele.replace(ball_position,'')
    print(f'cup_swapping({swap_list}) ➞ {ball_position}')
            
cup_swapping(["AB", "CA", "AB"],'B')
cup_swapping(["AB", "CA", "AB"],'C')
cup_swapping(["AC", "BC", "AB"],'A')

