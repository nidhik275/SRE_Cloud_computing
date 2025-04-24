'''
problem: expontential backup with Jitters
Author: Nidhi Kumari
Date: 21/04/2025
'''
import time
import random

class Solution:
        def api_call(self):
            return random.choice([False, True, False])
        
        def retry(self):
            maximum_backoff = 64
            code = self.api_call()
            
            if code == True: 
                print("Successful API call. Service is UP!")
            else:
                print(f"Error code {code} received.")

                for i in range(0,retry-1):
                    wait_time = min( (2**i) + random.randint(1, 20), maximum_backoff)
                    print(f"Retrying {i+1}...")
                    print(f"waiting for {wait_time} sec")
                    time.sleep(wait_time)
                    
                print(f"A successfull call after {retry} retries.")
                
        def exponential_backoff()
        
        
solution = Solution()
solution.exponential_backoff(4)           