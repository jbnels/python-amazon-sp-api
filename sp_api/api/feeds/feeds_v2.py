import urllib.parse

from sp_api.base import Client, sp_endpoint, fill_query_params, ApiResponse


class FeedsV2(Client):
    """
    Feeds SP-API Client
    :link: 

    The Selling Partner API for Feeds lets you upload data to Amazon on behalf of a selling partner.
    """


    @sp_endpoint('/feeds/2021-06-30/feeds', method='GET')
    def get_feeds(self, **kwargs) -> ApiResponse:
        """
        get_feeds(self, **kwargs) -> ApiResponse

        Returns feed details for the feeds that match the filters that you specify.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.0222 | 10 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            key feedTypes:array |  A list of feed types used to filter feeds. When feedTypes is provided, the other filter parameters (processingStatuses, marketplaceIds, createdSince, createdUntil) and pageSize may also be provided. Either feedTypes or nextToken is required.
        
            key marketplaceIds:array |  A list of marketplace identifiers used to filter feeds. The feeds returned will match at least one of the marketplaces that you specify.
        
            key pageSize:integer |  The maximum number of feeds to return in a single call.
        
            key processingStatuses:array |  A list of processing statuses used to filter feeds.
        
            key createdSince:string |  The earliest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is 90 days ago. Feeds are retained for a maximum of 90 days.
        
            key createdUntil:string |  The latest feed creation date and time for feeds included in the response, in ISO 8601 format. The default is now.
        
            key nextToken:string |  A string token returned in the response to your previous request. nextToken is returned when the number of results exceeds the specified pageSize value. To get the next page of results, call the getFeeds operation and include this token as the only parameter. Specifying nextToken with any other parameters will cause the request to fail.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  params=kwargs)
    

    @sp_endpoint('/feeds/2021-06-30/feeds', method='POST')
    def create_feed(self, feed_type, input_feed_document_id, **kwargs) -> ApiResponse:
        """
        create_feed(self, feed_type: str, input_feed_document_id: str, **kwargs) -> ApiResponse

        Creates a feed. Call `create_feed_document` to upload the feed first.
        `submit_feed` combines both.

        **Usage Plan:**

        ======================================  ==============
        Rate (requests per second)               Burst
        ======================================  ==============
        0.0083                                  15
        ======================================  ==============

        For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

        Examples:
            literal blocks::

                Feeds().create_feed('POST_PRODUCT_DATA', '3d4e42b5-1d6e-44e8-a89c-2abfca0625bb',
                              marketplaceIds=["ATVPDKIKX0DER", "A1F83G8C2ARO7P"])

        Args:
            feed_type: https://github.com/amzn/selling-partner-api-docs/blob/main/references/feeds-api/feedtype-values.md
            input_feed_document_id: str
            **kwargs:

        Returns:
            CreateFeedResponse:
        """
        data = {
            'feedType': feed_type,
            'inputFeedDocumentId': input_feed_document_id,
            **kwargs
        }
        return self._request(kwargs.pop('path'),  data=data)
    

    @sp_endpoint('/feeds/2021-06-30/feeds/{}', method='DELETE')
    def cancel_feed(self, feedId, **kwargs) -> ApiResponse:
        """
        cancel_feed(self, feedId, **kwargs) -> ApiResponse

        Cancels the feed that you specify. Only feeds with processingStatus=IN_QUEUE can be cancelled. Cancelled feeds are returned in subsequent calls to the getFeed and getFeeds operations.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.0222 | 10 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            feedId:string | * REQUIRED The identifier for the feed. This identifier is unique only in combination with a seller ID.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), feedId), data=kwargs)
    

    @sp_endpoint('/feeds/2021-06-30/feeds/{}', method='GET')
    def get_feed(self, feedId, **kwargs) -> ApiResponse:
        """
        get_feed(self, feedId, **kwargs) -> ApiResponse

        Returns feed details (including the resultDocumentId, if available) for the feed that you specify.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 2.0 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            feedId:string | * REQUIRED The identifier for the feed. This identifier is unique only in combination with a seller ID.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), feedId), params=kwargs)
    

    @sp_endpoint('/feeds/2021-06-30/documents', method='POST')
    def create_feed_document(self, **kwargs) -> ApiResponse:
        """
        create_feed_document(self, **kwargs) -> ApiResponse

        Creates a feed document for the feed type that you specify. This operation returns a presigned URL for uploading the feed document contents. It also returns a feedDocumentId value that you can pass in with a subsequent call to the createFeed operation.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.0083 | 15 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            body: | * REQUIRED {'description': 'Specifies the content type for the createFeedDocument operation.', 'properties': {'contentType': {'description': 'The content type of the feed.', 'type': 'string'}}, 'required': ['contentType'], 'type': 'object'}
        

         Returns:
            ApiResponse:
        """
    
        return self._request(kwargs.pop('path'),  data=kwargs)
    

    @sp_endpoint('/feeds/2021-06-30/documents/{}', method='GET')
    def get_feed_document(self, feedDocumentId, **kwargs) -> ApiResponse:
        """
        get_feed_document(self, feedDocumentId, **kwargs) -> ApiResponse

        Returns the information required for retrieving a feed document's contents.

**Usage Plan:**

| Rate (requests per second) | Burst |
| ---- | ---- |
| 0.0222 | 10 |

For more information, see "Usage Plans and Rate Limits" in the Selling Partner API documentation.

         Args:
        
            feedDocumentId:string | * REQUIRED The identifier of the feed document.
        

         Returns:
            ApiResponse:
        """
    
        return self._request(fill_query_params(kwargs.pop('path'), feedDocumentId), params=kwargs)
    
