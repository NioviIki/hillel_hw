In [1]: client = Client.objects.get(pk=1)
SELECT "catalog_client"."id",
       "catalog_client"."key_id"
  FROM "catalog_client"
 WHERE "catalog_client"."id" = 1
 LIMIT 21

Execution time: 0.001385s [Database: default]

In [2]: client.key
SELECT "catalog_city"."id",
       "catalog_city"."city"
  FROM "catalog_city"
 WHERE "catalog_city"."id" = 1
 LIMIT 21

Execution time: 0.000204s [Database: default]
Out[2]: <City: Dnipro>

In [3]: client.product.all()
Out[3]: SELECT "catalog_product"."id",
       "catalog_product"."product"
  FROM "catalog_product"
 INNER JOIN "catalog_client_product"
    ON ("catalog_product"."id" = "catalog_client_product"."product_id")
 WHERE "catalog_client_product"."client_id" = 1
 LIMIT 21

Execution time: 0.000217s [Database: default]
<QuerySet [<Product: Knife>]>

In [4]: retailer = Retailer.objects.get(pk=1)
SELECT "catalog_retailer"."id",
       "catalog_retailer"."company",
       "catalog_retailer"."city_id"
  FROM "catalog_retailer"
 WHERE "catalog_retailer"."id" = 1
 LIMIT 21

Execution time: 0.000325s [Database: default]

In [5]: retailer.city
SELECT "catalog_city"."id",
       "catalog_city"."city"
  FROM "catalog_city"
 WHERE "catalog_city"."id" = 1
 LIMIT 21

Execution time: 0.000245s [Database: default]
Out[5]: <City: Dnipro>
