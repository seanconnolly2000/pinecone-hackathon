query_preamble = """### MS SQL Server tables, with their properties:\n"""


sql_tables_all = """# [HumanResources].[Department](DepartmentID, Name, GroupName, ModifiedDate)
# [HumanResources].[Employee](BusinessEntityID, NationalIDNumber, LoginID, OrganizationNode, OrganizationLevel, JobTitle, BirthDate, MaritalStatus, Gender, HireDate, SalariedFlag, VacationHours, SickLeaveHours, CurrentFlag, rowguid, ModifiedDate)
# [HumanResources].[EmployeeDepartmentHistory](BusinessEntityID, DepartmentID, ShiftID, StartDate, EndDate, ModifiedDate)
# [HumanResources].[EmployeePayHistory](BusinessEntityID, RateChangeDate, Rate, PayFrequency, ModifiedDate)
# [HumanResources].[JobCandidate](JobCandidateID, BusinessEntityID, Resume, ModifiedDate)
# [HumanResources].[Shift](ShiftID, Name, StartTime, EndTime, ModifiedDate)
# [Person].[Address](AddressID, AddressLine1, AddressLine2, City, StateProvinceID, PostalCode, SpatialLocation, rowguid, ModifiedDate)
# [Person].[AddressType](AddressTypeID, Name, rowguid, ModifiedDate)
# [Person].[BusinessEntity](BusinessEntityID, rowguid, ModifiedDate)
# [Person].[BusinessEntityAddress](BusinessEntityID, AddressID, AddressTypeID, rowguid, ModifiedDate)
# [Person].[BusinessEntityContact](BusinessEntityID, PersonID, ContactTypeID, rowguid, ModifiedDate)
# [Person].[ContactType](ContactTypeID, Name, ModifiedDate)
# [Person].[CountryRegion](CountryRegionCode, Name, ModifiedDate)
# [Person].[EmailAddress](BusinessEntityID, EmailAddressID, EmailAddress, rowguid, ModifiedDate)
# [Person].[Person](BusinessEntityID, PersonType, NameStyle, Title, FirstName, MiddleName, LastName, Suffix, EmailPromotion, AdditionalContactInfo, Demographics, rowguid, ModifiedDate)
# [Person].[PersonPhone](BusinessEntityID, PhoneNumber, PhoneNumberTypeID, ModifiedDate)
# [Person].[PhoneNumberType](PhoneNumberTypeID, Name, ModifiedDate)
# [Person].[StateProvince](StateProvinceID, StateProvinceCode, CountryRegionCode, IsOnlyStateProvinceFlag, Name, TerritoryID, rowguid, ModifiedDate)
# [Production].[BillOfMaterials](BillOfMaterialsID, ProductAssemblyID, ComponentID, StartDate, EndDate, UnitMeasureCode, BOMLevel, PerAssemblyQty, ModifiedDate)
# [Production].[Culture](CultureID, Name, ModifiedDate)
# [Production].[Document](DocumentNode, DocumentLevel, Title, Owner, FolderFlag, FileName, FileExtension, Revision, ChangeNumber, Status, DocumentSummary, Document, rowguid, ModifiedDate)
# [Production].[Illustration](IllustrationID, Diagram, ModifiedDate)
# [Production].[Location](LocationID, Name, CostRate, Availability, ModifiedDate)
# [Production].[Product](ProductID, Name, ProductNumber, MakeFlag, FinishedGoodsFlag, Color, SafetyStockLevel, ReorderPoint, StandardCost, ListPrice, Size, SizeUnitMeasureCode, WeightUnitMeasureCode, Weight, DaysToManufacture, ProductLine, Class, Style, ProductSubcategoryID, ProductModelID, SellStartDate, SellEndDate, DiscontinuedDate, rowguid, ModifiedDate)
# [Production].[ProductCategory](ProductCategoryID, Name, rowguid, ModifiedDate)
# [Production].[ProductCostHistory](ProductID, StartDate, EndDate, StandardCost, ModifiedDate)
# [Production].[ProductDescription](ProductDescriptionID, Description, rowguid, ModifiedDate)
# [Production].[ProductDocument](ProductID, DocumentNode, ModifiedDate)
# [Production].[ProductInventory](ProductID, LocationID, Shelf, Bin, Quantity, rowguid, ModifiedDate)
# [Production].[ProductListPriceHistory](ProductID, StartDate, EndDate, ListPrice, ModifiedDate)
# [Production].[ProductModel](ProductModelID, Name, CatalogDescription, Instructions, rowguid, ModifiedDate)
# [Production].[ProductModelIllustration](ProductModelID, IllustrationID, ModifiedDate)
# [Production].[ProductModelProductDescriptionCulture](ProductModelID, ProductDescriptionID, CultureID, ModifiedDate)
# [Production].[ProductPhoto](ProductPhotoID, ThumbNailPhoto, ThumbnailPhotoFileName, LargePhoto, LargePhotoFileName, ModifiedDate)
# [Production].[ProductProductPhoto](ProductID, ProductPhotoID, Primary, ModifiedDate)
# [Production].[ProductReview](ProductReviewID, ProductID, ReviewerName, ReviewDate, EmailAddress, Rating, Comments, ModifiedDate)
# [Production].[ProductSubcategory](ProductSubcategoryID, ProductCategoryID, Name, rowguid, ModifiedDate)
# [Production].[ScrapReason](ScrapReasonID, Name, ModifiedDate)
# [Production].[TransactionHistory](TransactionID, ProductID, ReferenceOrderID, ReferenceOrderLineID, TransactionDate, TransactionType, Quantity, ActualCost, ModifiedDate)
# [Production].[TransactionHistoryArchive](TransactionID, ProductID, ReferenceOrderID, ReferenceOrderLineID, TransactionDate, TransactionType, Quantity, ActualCost, ModifiedDate)
# [Production].[UnitMeasure](UnitMeasureCode, Name, ModifiedDate)
# [Production].[WorkOrder](WorkOrderID, ProductID, OrderQty, StockedQty, ScrappedQty, StartDate, EndDate, DueDate, ScrapReasonID, ModifiedDate)
# [Production].[WorkOrderRouting](WorkOrderID, ProductID, OperationSequence, LocationID, ScheduledStartDate, ScheduledEndDate, ActualStartDate, ActualEndDate, ActualResourceHrs, PlannedCost, ActualCost, ModifiedDate)
# [Purchasing].[ProductVendor](ProductID, BusinessEntityID, AverageLeadTime, StandardPrice, LastReceiptCost, LastReceiptDate, MinOrderQty, MaxOrderQty, OnOrderQty, UnitMeasureCode, ModifiedDate)
# [Purchasing].[PurchaseOrderDetail](PurchaseOrderID, PurchaseOrderDetailID, DueDate, OrderQty, ProductID, UnitPrice, LineTotal, ReceivedQty, RejectedQty, StockedQty, ModifiedDate)
# [Purchasing].[PurchaseOrderHeader](PurchaseOrderID, RevisionNumber, Status, EmployeeID, VendorID, ShipMethodID, OrderDate, ShipDate, SubTotal, TaxAmt, Freight, TotalDue, ModifiedDate)
# [Purchasing].[ShipMethod](ShipMethodID, Name, ShipBase, ShipRate, rowguid, ModifiedDate)
# [Purchasing].[Vendor](BusinessEntityID, AccountNumber, Name, CreditRating, PreferredVendorStatus, ActiveFlag, PurchasingWebServiceURL, ModifiedDate)
# [Sales].[CountryRegionCurrency](CountryRegionCode, CurrencyCode, ModifiedDate)
# [Sales].[CreditCard](CreditCardID, CardType, CardNumber, ExpMonth, ExpYear, ModifiedDate)
# [Sales].[Currency](CurrencyCode, Name, ModifiedDate)
# [Sales].[CurrencyRate](CurrencyRateID, CurrencyRateDate, FromCurrencyCode, ToCurrencyCode, AverageRate, EndOfDayRate, ModifiedDate)
# [Sales].[Customer](CustomerID, PersonID, StoreID, TerritoryID, AccountNumber, rowguid, ModifiedDate)
# [Sales].[PersonCreditCard](BusinessEntityID, CreditCardID, ModifiedDate)
# [Sales].[SalesOrderDetail](SalesOrderID, SalesOrderDetailID, CarrierTrackingNumber, OrderQty, ProductID, SpecialOfferID, UnitPrice, UnitPriceDiscount, LineTotal, rowguid, ModifiedDate)
# [Sales].[SalesOrderHeader](SalesOrderID, RevisionNumber, OrderDate, DueDate, ShipDate, Status, OnlineOrderFlag, SalesOrderNumber, PurchaseOrderNumber, AccountNumber, CustomerID, SalesPersonID, TerritoryID, BillToAddressID, ShipToAddressID, ShipMethodID, CreditCardID, CreditCardApprovalCode, CurrencyRateID, SubTotal, TaxAmt, Freight, TotalDue, Comment, rowguid, ModifiedDate)
# [Sales].[SalesOrderHeaderSalesReason](SalesOrderID, SalesReasonID, ModifiedDate)
# [Sales].[SalesPerson](BusinessEntityID, TerritoryID, SalesQuota, Bonus, CommissionPct, SalesYTD, SalesLastYear, rowguid, ModifiedDate)
# [Sales].[SalesPersonQuotaHistory](BusinessEntityID, QuotaDate, SalesQuota, rowguid, ModifiedDate)
# [Sales].[SalesReason](SalesReasonID, Name, ReasonType, ModifiedDate)
# [Sales].[SalesTaxRate](SalesTaxRateID, StateProvinceID, TaxType, TaxRate, Name, rowguid, ModifiedDate)
# [Sales].[SalesTerritory](TerritoryID, Name, CountryRegionCode, Group, SalesYTD, SalesLastYear, CostYTD, CostLastYear, rowguid, ModifiedDate)
# [Sales].[SalesTerritoryHistory](BusinessEntityID, TerritoryID, StartDate, EndDate, rowguid, ModifiedDate)
# [Sales].[ShoppingCartItem](ShoppingCartItemID, ShoppingCartID, Quantity, ProductID, DateCreated, ModifiedDate)
# [Sales].[SpecialOffer](SpecialOfferID, Description, DiscountPct, Type, Category, StartDate, EndDate, MinQty, MaxQty, rowguid, ModifiedDate)
# [Sales].[SpecialOfferProduct](SpecialOfferID, ProductID, rowguid, ModifiedDate)
# [Sales].[Store](BusinessEntityID, Name, SalesPersonID, Demographics, rowguid, ModifiedDate)
"""



sql_tables_sales = """# [Sales].[CountryRegionCurrency](CountryRegionCode, CurrencyCode, ModifiedDate)
# [Sales].[CreditCard](CreditCardID, CardType, CardNumber, ExpMonth, ExpYear, ModifiedDate)
# [Sales].[Currency](CurrencyCode, Name, ModifiedDate)
# [Sales].[CurrencyRate](CurrencyRateID, CurrencyRateDate, FromCurrencyCode, ToCurrencyCode, AverageRate, EndOfDayRate, ModifiedDate)
# [Sales].[Customer](CustomerID, PersonID, StoreID, TerritoryID, AccountNumber, rowguid, ModifiedDate)
# [Sales].[PersonCreditCard](BusinessEntityID, CreditCardID, ModifiedDate)
# [Sales].[SalesOrderHeader](SalesOrderID, RevisionNumber, OrderDate, DueDate, ShipDate, Status, OnlineOrderFlag, SalesOrderNumber, PurchaseOrderNumber, AccountNumber, CustomerID, SalesPersonID, TerritoryID, BillToAddressID, ShipToAddressID, ShipMethodID, CreditCardID, CreditCardApprovalCode, CurrencyRateID, SubTotal, TaxAmt, Freight, TotalDue, Comment, rowguid, ModifiedDate)
# [Sales].[SalesOrderDetail](SalesOrderID, SalesOrderDetailID, CarrierTrackingNumber, OrderQty, ProductID, SpecialOfferID, UnitPrice, UnitPriceDiscount, LineTotal, rowguid, ModifiedDate)
# [Sales].[SalesOrderHeaderSalesReason](SalesOrderID, SalesReasonID, ModifiedDate)
# [Sales].[SalesPerson](BusinessEntityID, TerritoryID, SalesQuota, Bonus, CommissionPct, SalesYTD, SalesLastYear, rowguid, ModifiedDate)
# [Sales].[SalesPersonQuotaHistory](BusinessEntityID, QuotaDate, SalesQuota, rowguid, ModifiedDate)
# [Sales].[SalesReason](SalesReasonID, Name, ReasonType, ModifiedDate)
# [Sales].[SalesTaxRate](SalesTaxRateID, StateProvinceID, TaxType, TaxRate, Name, rowguid, ModifiedDate)
# [Sales].[SalesTerritory](TerritoryID, Name, CountryRegionCode, Group, SalesYTD, SalesLastYear, CostYTD, CostLastYear, rowguid, ModifiedDate)
# [Sales].[SalesTerritoryHistory](BusinessEntityID, TerritoryID, StartDate, EndDate, rowguid, ModifiedDate)
# [Sales].[ShoppingCartItem](ShoppingCartItemID, ShoppingCartID, Quantity, ProductID, DateCreated, ModifiedDate)
# [Sales].[SpecialOffer](SpecialOfferID, Description, DiscountPct, Type, Category, StartDate, EndDate, MinQty, MaxQty, rowguid, ModifiedDate)
# [Sales].[SpecialOfferProduct](SpecialOfferID, ProductID, rowguid, ModifiedDate)
# [Sales].[Store](BusinessEntityID, Name, SalesPersonID, Demographics, rowguid, ModifiedDate)
# [Person].[Address](AddressID, AddressLine1, AddressLine2, City, StateProvinceID, PostalCode, SpatialLocation, rowguid, ModifiedDate)
# [Person].[AddressType](AddressTypeID, Name, rowguid, ModifiedDate)
# [Person].[BusinessEntity](BusinessEntityID, rowguid, ModifiedDate)
# [Person].[BusinessEntityAddress](BusinessEntityID, AddressID, AddressTypeID, rowguid, ModifiedDate)
# [Person].[BusinessEntityContact](BusinessEntityID, PersonID, ContactTypeID, rowguid, ModifiedDate)
# [Person].[ContactType](ContactTypeID, Name, ModifiedDate)
# [Person].[CountryRegion](CountryRegionCode, Name, ModifiedDate)
# [Person].[EmailAddress](BusinessEntityID, EmailAddressID, EmailAddress, rowguid, ModifiedDate)
# [Person].[Person](BusinessEntityID, PersonType, NameStyle, Title, FirstName, MiddleName, LastName, Suffix, EmailPromotion, AdditionalContactInfo, Demographics, rowguid, ModifiedDate)
# [Person].[PersonPhone](BusinessEntityID, PhoneNumber, PhoneNumberTypeID, ModifiedDate)
# [Person].[PhoneNumberType](PhoneNumberTypeID, Name, ModifiedDate)
# [Person].[StateProvince](StateProvinceID, StateProvinceCode, CountryRegionCode, IsOnlyStateProvinceFlag, Name, TerritoryID, rowguid, ModifiedDate)
"""


sql_tables_production = """# [Production].[BillOfMaterials](BillOfMaterialsID, ProductAssemblyID, ComponentID, StartDate, EndDate, UnitMeasureCode, BOMLevel, PerAssemblyQty, ModifiedDate)
# [Production].[Culture](CultureID, Name, ModifiedDate)
# [Production].[Document](DocumentNode, DocumentLevel, Title, Owner, FolderFlag, FileName, FileExtension, Revision, ChangeNumber, Status, DocumentSummary, Document, rowguid, ModifiedDate)
# [Production].[Illustration](IllustrationID, Diagram, ModifiedDate)
# [Production].[Location](LocationID, Name, CostRate, Availability, ModifiedDate)
# [Production].[Product](ProductID, Name, ProductNumber, MakeFlag, FinishedGoodsFlag, Color, SafetyStockLevel, ReorderPoint, StandardCost, ListPrice, Size, SizeUnitMeasureCode, WeightUnitMeasureCode, Weight, DaysToManufacture, ProductLine, Class, Style, ProductSubcategoryID, ProductModelID, SellStartDate, SellEndDate, DiscontinuedDate, rowguid, ModifiedDate)
# [Production].[ProductCategory](ProductCategoryID, Name, rowguid, ModifiedDate)
# [Production].[ProductCostHistory](ProductID, StartDate, EndDate, StandardCost, ModifiedDate)
# [Production].[ProductDescription](ProductDescriptionID, Description, rowguid, ModifiedDate)
# [Production].[ProductDocument](ProductID, DocumentNode, ModifiedDate)
# [Production].[ProductInventory](ProductID, LocationID, Shelf, Bin, Quantity, rowguid, ModifiedDate)
# [Production].[ProductListPriceHistory](ProductID, StartDate, EndDate, ListPrice, ModifiedDate)
# [Production].[ProductModel](ProductModelID, Name, CatalogDescription, Instructions, rowguid, ModifiedDate)
# [Production].[ProductModelIllustration](ProductModelID, IllustrationID, ModifiedDate)
# [Production].[ProductModelProductDescriptionCulture](ProductModelID, ProductDescriptionID, CultureID, ModifiedDate)
# [Production].[ProductPhoto](ProductPhotoID, ThumbNailPhoto, ThumbnailPhotoFileName, LargePhoto, LargePhotoFileName, ModifiedDate)
# [Production].[ProductProductPhoto](ProductID, ProductPhotoID, Primary, ModifiedDate)
# [Production].[ProductReview](ProductReviewID, ProductID, ReviewerName, ReviewDate, EmailAddress, Rating, Comments, ModifiedDate)
# [Production].[ProductSubcategory](ProductSubcategoryID, ProductCategoryID, Name, rowguid, ModifiedDate)
# [Production].[ScrapReason](ScrapReasonID, Name, ModifiedDate)
# [Production].[TransactionHistory](TransactionID, ProductID, ReferenceOrderID, ReferenceOrderLineID, TransactionDate, TransactionType, Quantity, ActualCost, ModifiedDate)
# [Production].[TransactionHistoryArchive](TransactionID, ProductID, ReferenceOrderID, ReferenceOrderLineID, TransactionDate, TransactionType, Quantity, ActualCost, ModifiedDate)
# [Production].[UnitMeasure](UnitMeasureCode, Name, ModifiedDate)
# [Production].[WorkOrder](WorkOrderID, ProductID, OrderQty, StockedQty, ScrappedQty, StartDate, EndDate, DueDate, ScrapReasonID, ModifiedDate)
# [Production].[WorkOrderRouting](WorkOrderID, ProductID, OperationSequence, LocationID, ScheduledStartDate, ScheduledEndDate, ActualStartDate, ActualEndDate, ActualResourceHrs, PlannedCost, ActualCost, ModifiedDate)
# [HumanResources].[Department](DepartmentID, Name, GroupName, ModifiedDate)
# [HumanResources].[Employee](BusinessEntityID, NationalIDNumber, LoginID, OrganizationNode, OrganizationLevel, JobTitle, BirthDate, MaritalStatus, Gender, HireDate, SalariedFlag, VacationHours, SickLeaveHours, CurrentFlag, rowguid, ModifiedDate)
# [HumanResources].[EmployeeDepartmentHistory](BusinessEntityID, DepartmentID, ShiftID, StartDate, EndDate, ModifiedDate)
# [HumanResources].[EmployeePayHistory](BusinessEntityID, RateChangeDate, Rate, PayFrequency, ModifiedDate)
# [HumanResources].[JobCandidate](JobCandidateID, BusinessEntityID, Resume, ModifiedDate)
# [HumanResources].[Shift](ShiftID, Name, StartTime, EndTime, ModifiedDate)
# [Person].[Address](AddressID, AddressLine1, AddressLine2, City, StateProvinceID, PostalCode, SpatialLocation, rowguid, ModifiedDate)
# [Person].[AddressType](AddressTypeID, Name, rowguid, ModifiedDate)
# [Person].[BusinessEntity](BusinessEntityID, rowguid, ModifiedDate)
# [Person].[BusinessEntityAddress](BusinessEntityID, AddressID, AddressTypeID, rowguid, ModifiedDate)
# [Person].[BusinessEntityContact](BusinessEntityID, PersonID, ContactTypeID, rowguid, ModifiedDate)
# [Person].[ContactType](ContactTypeID, Name, ModifiedDate)
# [Person].[CountryRegion](CountryRegionCode, Name, ModifiedDate)
# [Person].[EmailAddress](BusinessEntityID, EmailAddressID, EmailAddress, rowguid, ModifiedDate)
# [Person].[Person](BusinessEntityID, PersonType, NameStyle, Title, FirstName, MiddleName, LastName, Suffix, EmailPromotion, AdditionalContactInfo, Demographics, rowguid, ModifiedDate)
# [Person].[PersonPhone](BusinessEntityID, PhoneNumber, PhoneNumberTypeID, ModifiedDate)
# [Person].[PhoneNumberType](PhoneNumberTypeID, Name, ModifiedDate)
# [Person].[StateProvince](StateProvinceID, StateProvinceCode, CountryRegionCode, IsOnlyStateProvinceFlag, Name, TerritoryID, rowguid, ModifiedDate)
"""


sql_tables_purchasing = """# [Purchasing].[ProductVendor](ProductID, BusinessEntityID, AverageLeadTime, StandardPrice, LastReceiptCost, LastReceiptDate, MinOrderQty, MaxOrderQty, OnOrderQty, UnitMeasureCode, ModifiedDate)
# [Purchasing].[PurchaseOrderDetail](PurchaseOrderID, PurchaseOrderDetailID, DueDate, OrderQty, ProductID, UnitPrice, LineTotal, ReceivedQty, RejectedQty, StockedQty, ModifiedDate)
# [Purchasing].[PurchaseOrderHeader](PurchaseOrderID, RevisionNumber, Status, EmployeeID, VendorID, ShipMethodID, OrderDate, ShipDate, SubTotal, TaxAmt, Freight, TotalDue, ModifiedDate)
# [Purchasing].[ShipMethod](ShipMethodID, Name, ShipBase, ShipRate, rowguid, ModifiedDate)
# [Purchasing].[Vendor](BusinessEntityID, AccountNumber, Name, CreditRating, PreferredVendorStatus, ActiveFlag, PurchasingWebServiceURL, ModifiedDate)
# [HumanResources].[Department](DepartmentID, Name, GroupName, ModifiedDate)
# [HumanResources].[Employee](BusinessEntityID, NationalIDNumber, LoginID, OrganizationNode, OrganizationLevel, JobTitle, BirthDate, MaritalStatus, Gender, HireDate, SalariedFlag, VacationHours, SickLeaveHours, CurrentFlag, rowguid, ModifiedDate)
# [HumanResources].[EmployeeDepartmentHistory](BusinessEntityID, DepartmentID, ShiftID, StartDate, EndDate, ModifiedDate)
# [Person].[Address](AddressID, AddressLine1, AddressLine2, City, StateProvinceID, PostalCode, SpatialLocation, rowguid, ModifiedDate)
# [Person].[AddressType](AddressTypeID, Name, rowguid, ModifiedDate)
# [Person].[BusinessEntity](BusinessEntityID, rowguid, ModifiedDate)
# [Person].[BusinessEntityAddress](BusinessEntityID, AddressID, AddressTypeID, rowguid, ModifiedDate)
# [Person].[BusinessEntityContact](BusinessEntityID, PersonID, ContactTypeID, rowguid, ModifiedDate)
# [Person].[ContactType](ContactTypeID, Name, ModifiedDate)
# [Person].[CountryRegion](CountryRegionCode, Name, ModifiedDate)
# [Person].[EmailAddress](BusinessEntityID, EmailAddressID, EmailAddress, rowguid, ModifiedDate)
# [Person].[Person](BusinessEntityID, PersonType, NameStyle, Title, FirstName, MiddleName, LastName, Suffix, EmailPromotion, AdditionalContactInfo, Demographics, rowguid, ModifiedDate)
# [Person].[PersonPhone](BusinessEntityID, PhoneNumber, PhoneNumberTypeID, ModifiedDate)
# [Person].[PhoneNumberType](PhoneNumberTypeID, Name, ModifiedDate)
# [Person].[StateProvince](StateProvinceID, StateProvinceCode, CountryRegionCode, IsOnlyStateProvinceFlag, Name, TerritoryID, rowguid, ModifiedDate)
"""


sql_tables_hr = """# [HumanResources].[Department](DepartmentID, Name, GroupName, ModifiedDate)
# [HumanResources].[Employee](BusinessEntityID, NationalIDNumber, LoginID, OrganizationNode, OrganizationLevel, JobTitle, BirthDate, MaritalStatus, Gender, HireDate, SalariedFlag, VacationHours, SickLeaveHours, CurrentFlag, rowguid, ModifiedDate)
# [HumanResources].[EmployeeDepartmentHistory](BusinessEntityID, DepartmentID, ShiftID, StartDate, EndDate, ModifiedDate)
# [HumanResources].[EmployeePayHistory](BusinessEntityID, RateChangeDate, Rate, PayFrequency, ModifiedDate)
# [HumanResources].[JobCandidate](JobCandidateID, BusinessEntityID, Resume, ModifiedDate)
# [HumanResources].[Shift](ShiftID, Name, StartTime, EndTime, ModifiedDate)
# [Person].[Address](AddressID, AddressLine1, AddressLine2, City, StateProvinceID, PostalCode, SpatialLocation, rowguid, ModifiedDate)
# [Person].[AddressType](AddressTypeID, Name, rowguid, ModifiedDate)
# [Person].[BusinessEntity](BusinessEntityID, rowguid, ModifiedDate)
# [Person].[BusinessEntityAddress](BusinessEntityID, AddressID, AddressTypeID, rowguid, ModifiedDate)
# [Person].[BusinessEntityContact](BusinessEntityID, PersonID, ContactTypeID, rowguid, ModifiedDate)
# [Person].[ContactType](ContactTypeID, Name, ModifiedDate)
# [Person].[CountryRegion](CountryRegionCode, Name, ModifiedDate)
# [Person].[EmailAddress](BusinessEntityID, EmailAddressID, EmailAddress, rowguid, ModifiedDate)
# [Person].[Person](BusinessEntityID, PersonType, NameStyle, Title, FirstName, MiddleName, LastName, Suffix, EmailPromotion, AdditionalContactInfo, Demographics, rowguid, ModifiedDate)
# [Person].[PersonPhone](BusinessEntityID, PhoneNumber, PhoneNumberTypeID, ModifiedDate)
# [Person].[PhoneNumberType](PhoneNumberTypeID, Name, ModifiedDate)
# [Person].[StateProvince](StateProvinceID, StateProvinceCode, CountryRegionCode, IsOnlyStateProvinceFlag, Name, TerritoryID, rowguid, ModifiedDate)
"""

















#SQL TO GENERATE THE ABOVE LIST:

#https://learn.microsoft.com/en-us/answers/questions/1198902/how-to-extract-create-table-script-for-a-given-tab?orderby=newest
#Declare @object_id int;
#Declare @object_name varchar(500);
#DECLARE @SQL NVARCHAR(MAX) = ''

#DECLARE Cur1 CURSOR FOR
#    SELECT 
#     '[' + s.name + '].[' + o.name + ']', o.[object_id]
#		FROM sys.objects o WITH (NOWAIT)
#		JOIN sys.schemas s WITH (NOWAIT) ON o.[schema_id] = s.[schema_id]
#		WHERE o.[type] = 'U'
#			AND o.is_ms_shipped = 0
#			AND s.name != 'dbo'

#OPEN Cur1
#FETCH NEXT FROM Cur1 INTO @object_name, @object_id;
#PRINT('### MS SQL Server tables, with their properties:')
#WHILE @@FETCH_STATUS = 0
#BEGIN
#	SELECT @SQL = '# '  + @object_name + '(' 
#    SELECT @SQL = @SQL +  '' + c.name + ', ' 
#    FROM sys.columns c WITH (NOWAIT)
#    JOIN sys.types tp WITH (NOWAIT) ON c.user_type_id = tp.user_type_id
#    LEFT JOIN sys.computed_columns cc WITH (NOWAIT) ON c.[object_id] = cc.[object_id] AND c.column_id = cc.column_id
#    LEFT JOIN sys.default_constraints dc WITH (NOWAIT) ON c.default_object_id != 0 AND c.[object_id] = dc.parent_object_id AND c.column_id = dc.parent_column_id
#    LEFT JOIN sys.identity_columns ic WITH (NOWAIT) ON c.is_identity = 1 AND c.[object_id] = ic.[object_id] AND c.column_id = ic.column_id
#    WHERE c.[object_id] =  @object_id
#	SELECT @SQL = @SQL +  ')' 
#	PRINT(@SQL)
#    FETCH NEXT FROM Cur1 INTO @object_name, @object_id;
#END;
#CLOSE Cur1;
#DEALLOCATE Cur1;




##############################################################################
# THIS WILL UPDATE YOUR ADVENTUREWORKS DATABASE AND BRING IT FORWARD 7 YEARS SO IT ISN'T SO OLD


#Declare @object_id int;
#Declare @object_name varchar(500);
#DECLARE @SQL NVARCHAR(MAX) = ''

#DECLARE Cur1 CURSOR FOR
#    SELECT 
#     '[' + s.name + '].[' + o.name + ']', o.[object_id]
#		FROM sys.objects o WITH (NOWAIT)
#		JOIN sys.schemas s WITH (NOWAIT) ON o.[schema_id] = s.[schema_id]
#		WHERE o.[type] = 'U'
#			AND o.is_ms_shipped = 0
#			AND s.name != 'dbo'
#		ORDER BY s.name, o.name

#OPEN Cur1
#FETCH NEXT FROM Cur1 INTO @object_name, @object_id;

#WHILE @@FETCH_STATUS = 0
#BEGIN
#    SELECT @SQL = @SQL + 'UPDATE ' + @object_name + ' SET ' + c.name + ' = dateadd(yy,7, ' + c.name + ')' 
#    FROM sys.columns c WITH (NOWAIT)
#    JOIN sys.types tp WITH (NOWAIT) ON c.user_type_id = tp.user_type_id
#    LEFT JOIN sys.computed_columns cc WITH (NOWAIT) ON c.[object_id] = cc.[object_id] AND c.column_id = cc.column_id
#    LEFT JOIN sys.default_constraints dc WITH (NOWAIT) ON c.default_object_id != 0 AND c.[object_id] = dc.parent_object_id AND c.column_id = dc.parent_column_id
#    LEFT JOIN sys.identity_columns ic WITH (NOWAIT) ON c.is_identity = 1 AND c.[object_id] = ic.[object_id] AND c.column_id = ic.column_id
#    WHERE c.[object_id] =  @object_id
#	AND lower(c.name) like '%date' 
#	PRINT(@SQL)
#	SELECT @SQL = ''
#    FETCH NEXT FROM Cur1 INTO @object_name, @object_id;
#END;
#CLOSE Cur1;
#DEALLOCATE Cur1;







