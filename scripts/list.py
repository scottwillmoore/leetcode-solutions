# pyright: reportUnknownMemberType = none


from __future__ import annotations

from asyncio import run
from dataclasses import dataclass
import os
import re

from gql import gql
from gql.client import Client as GraphQLClient, AsyncClientSession as GraphQLSession
from gql.transport.aiohttp import AIOHTTPTransport


@dataclass(frozen=True, kw_only=True)
class Question:
    difficulty: str
    dislikes: int
    index: int
    likes: int
    title: str
    title_slug: str


apiEndpoint = "https://leetcode.com/graphql/"


class LeetCodeClient:
    csrf_token: str | None
    session_id: str | None

    client: GraphQLClient

    leetCodeSession: LeetCodeSession | None

    def __init__(self, *, csrf_token: str | None = None, session_id: str | None = None) -> None:
        self.csrf_token = csrf_token
        self.session_id = session_id

        cookies = {}
        headers = {}
        transport = AIOHTTPTransport(apiEndpoint, cookies=cookies, headers=headers)
        self.client = GraphQLClient(transport=transport)

        self.session = None

    async def __aenter__(self) -> LeetCodeSession:
        return await self.connect()

    async def __aexit__(self, _type, _value, _traceback_type) -> None:  # pyright: ignore
        await self.disconnect()

    async def connect(self) -> LeetCodeSession:
        session = await self.client.connect_async(reconnecting=True)  # pyright: ignore
        return LeetCodeSession(session)

    async def disconnect(self) -> None:
        await self.client.close_async()
        self.session = None


questionTitleQuery = gql(
    """
    query questionTitle($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionId
            questionFrontendId
            title
            titleSlug
            isPaidOnly
            difficulty
            likes
            dislikes
        }
    }
    """
)


class LeetCodeSession:
    session: GraphQLSession

    def __init__(self, session: GraphQLSession) -> None:
        self.session = session

    async def get_question(self, title_slug: str) -> Question:
        assert self.session

        response = await self.session.execute(questionTitleQuery, {"titleSlug": title_slug})

        assert response["question"]

        question = Question(
            difficulty=response["question"]["difficulty"],
            dislikes=int(response["question"]["dislikes"]),
            index=int(response["question"]["questionFrontendId"]),
            likes=int(response["question"]["likes"]),
            title=response["question"]["title"],
            title_slug=title_slug,
        )

        return question


filePattern = re.compile(r"^(\d{4})_(.+)$")


async def list_solutions(session: LeetCodeSession) -> None:
    solutions_path = os.path.join(os.getcwd(), "solutions")
    for solution_path in os.listdir(solutions_path):
        (base, extension) = os.path.splitext(solution_path)
        if extension != ".py":
            raise ValueError

        match = filePattern.match(base)
        if not match:
            raise ValueError

        index = int(match[1])
        title_slug = match[2].replace("_", "-")

        question = await session.get_question(title_slug)
        if index == question.index:
            print(f"Y: {question.title}")
        else:
            print(f"N: {question.title} ({index} != {question.index})")


async def main() -> None:
    client = LeetCodeClient()

    async with client as session:
        await list_solutions(session)


if __name__ == "__main__":
    run(main())
