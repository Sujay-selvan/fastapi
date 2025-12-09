from fastapi import FastAPI,HTTPException

def get_all_record(db,model):
    """
    _summary_

    Args:
        model (_type_): which model you want to get a data

    Returns:
        _type_: returns what i get 
    """
    return db.query(model).all()

def insert_record(db,model,object):
    """
    get a db,model,object from where this function called 
    and insert the table what they give the table
    return the response
    Args:
        db (Session): db session
        model (class): table name
        object (object): what data going to insert

    Returns:
        object or pydantic model: return the success response
    """
    insert_rec = model(**object.dict()) # convert pydantic model into dict
    db.add(insert_rec)
    db.commit()
    db.refresh(insert_rec)
    return insert_rec

def get_single_record(db,model,record_id):
    
    return db.query(model).filter(model.id == record_id).first()

def update_record(db,model,record_id,object):
    """_summary_

    Args:
        db (_type_): db session
        model (_type_): which model going to update
        record_id (_type_): for unique value
        object (_type_): what going to update

    Raises:
        HTTPException: raise a exception when the record not exist

    Returns:
        _type_: updated response
    """
    exist_record = db.query(model).filter(model.id == record_id).first()
    if not exist_record:
       raise HTTPException(status_code=400,detail="record not exist")
   
    if hasattr(object,"dict"):
        updated_object = object.dict(exclude_unset=True)
    
    for key, value in updated_object.items():
        setattr(exist_record,key,value)
    
    db.add(exist_record)
    db.commit()
    db.refresh(exist_record)
    return exist_record
    

def delete_record(db,model,record_id):
    """_summary_

    Args:
        db (_type_): db session
        model (_type_): which model to delete
        record_id (_type_): unique value
    """
    response = db.query(model).filter(model.id == record_id).first()
    if response:
        HTTPException(status_code=500,detail="invlaid record")
        db.delete(response)
        db.commit()
        return True
    raise HTTPException(status_code=500,detail="record not exist")