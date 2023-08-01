def chunking_by(numbers, chunck):

    new_chunck = []  #empty list to store the chunks
    if not numbers:   #if the list is empty, function returns an empty list
        return []

    num_chunks = len(numbers) // chunck  #number of chunks that the list can split into
    last_chunk_size = len(numbers) % chunck  #calculates the size of the last chunk
  
    for i in range(num_chunks):
        new_chunck.append(numbers[i * chunck:(i + 1) * chunck])

    if last_chunk_size > 0:    # if len(numbers) % chunck is > 0 ,it will add the remaining elements to the new chunck
        new_chunck.append(numbers[num_chunks * chunck:]) 

    return new_chunck
