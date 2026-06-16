from api.database.models import Users



def create_user_repo(db, user):
    db_user = Users(
        uuid=user._uuid,
        name=user.name,
        email=user.email,
        password_hash=user.password,
        created_at=user._created_at
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


def get_user_by_email_repo(db, email):
    user = db.query(Users).filter(Users.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user