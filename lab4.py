import hashlib

def sha256(data):
    """"return the SHA-256 hash of the given data"""
    return hashlib.sha256(data.encode('utf-8')).hexdigest() # Changed 'utf'-8 to 'utf-8'

def combine_and_hash(hash1,hash2):
    """combine two hashes and return their SHA-256 hash."""
    combine =hash1+hash2
    return sha256(combine)

# text parts provide
part1="And now the end is here And so I face that final curtain My friend I'll make it clearI'll state my case, of which I'm certainI've lived a life that's fullI traveled each and every highway And more, much more I did it, I did it my way"
part2="Regrets, I've had a few But then again too few to mention I did what I had to doI saw it through without exemptionI planned each charted courseEach careful step along the byway And more, much, much more I did it, I did it my way"
part3="Yes, there were times I'm sure you knew When I bit off more than I could chew But through it all, when there was doubt I ate it up and spit it out I faced it all and I stood tall and did it my way"
part4="For what is a man, what has he got? If not himself then he has naught Not to say the things that he truly feels And not the words of someone who kneels Let the record shows I took all the blows and did it my way"

#calculate the SHA-256 hashes for each part
hash1=sha256(part1)
hash2=sha256(part2)
hash3=sha256(part3)
hash4=sha256(part4)

print("hash of part 1:",hash1)
print("hash of part 2:",hash2)
print("hash of part 3:",hash3)
print("hash of part 4:",hash4)

#combine and hash the pairs
hash12=combine_and_hash(hash1,hash2)
hash34=combine_and_hash(hash3,hash4)

print("\ncombined hash of part 1 and part 2:",hash12)
print("combined hash of part 1 and part 4:",hash34)

#combine the resulting hashes to get the merkle root
merkle_root=combine_and_hash(hash1,hash34)

print("\nmerkle root:",merkle_root)